# train a LeNet5 model with local MNIST
from torchvision import datasets,transforms
from torch.utils.data import Dataset, DataLoader, sampler, Subset
import torch
from lenet5 import LeNet5
import time
import redis
import pickle
import numpy as np
from PIL import Image
import sys

def check_accuracy(loader, model):
  if loader.dataset.train:
      print('Checking accuracy on validation set')
  else:
      print('Checking accuracy on test set')
  num_correct = 0
  num_samples = 0
  model.eval()   # set model to evaluation mode
  with torch.no_grad():
    for x,y in loader:
      x = x.to(device=device)
      y = y.to(device=device)
      _, y_prob = model(x)
      _, preds = y_prob.max(1)
      num_correct += (preds==y).sum()
      num_samples += preds.size(0)
    acc = float(num_correct) / num_samples
    print('Got {} / {} correct {:.2f}'.format(num_correct, num_samples, 100 *acc))
    return acc

class RedisMnist(Dataset):
    def __init__(self,
                 redis_host='10.10.1.3',
                 redis_port=6379,
                 length=60000,
                 transform=None,
                 train=False):

        self.db = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
        self.length = length
        self.transform = transform
        self.train = train

    def __getitem__(self, index):
        objName = f'object{index}'
        data = self.db.hget('mnist', objName)
        data = pickle.loads(data.encode('latin1'))
        x_array = np.array(data['img'][0])
        x = x_array.reshape(28, 28).astype(np.uint8)
        x = Image.fromarray(x, mode='L')
        y = torch.tensor(data['label'][0]).long()
        if self.transform:
            x = self.transform(x)

        return x, y

    def __len__(self):
        return self.length

n_train = 50000
num_workers = int(sys.argv[1])
batch_size = int(sys.argv[2])

transform = transforms.Compose([transforms.Resize((32, 32)), 
                                transforms.ToTensor()])

start = time.time()
trainingSet = RedisMnist(transform=transform, train=True)
trainingLoader = DataLoader(dataset=trainingSet, batch_size=batch_size, sampler=sampler.SubsetRandomSampler(range(n_train)), num_workers=num_workers)

valLoader = DataLoader(trainingSet, batch_size=batch_size, sampler=sampler.SubsetRandomSampler(range(n_train, 60000)), num_workers=num_workers)
testSet = datasets.MNIST(root='/home/MNIST', train=False, transform=transform)
testLoader = DataLoader(dataset=testSet, batch_size=64, shuffle=False)

# pre-trained ResNet50 in PyTorch and modify the output layer (fc)
device = torch.device('cpu')

model = LeNet5(10).to(device)
lossFunc = torch.nn.CrossEntropyLoss()
opt = torch.optim.Adam(model.parameters(), lr=0.001)


# begin to train
num_epoch = 5
for epoch in range(num_epoch):
  running_loss = 0
  model.train()
  for step, data in enumerate(trainingLoader, start=0):
    images, labels = data
    images = images.to(device)
    labels = labels.to(device)
    pred, _ = model(images)
    loss = lossFunc(pred, labels)
    opt.zero_grad()
    loss.backward()
    opt.step()

    # print information
    running_loss += loss.item()
    rate = (step + 1) / len(trainingLoader)
    a = "*" * int(rate * 50)
    b = "." * int((1 - rate) * 50)
    #print("\rtrain loss: {:^3.0f}%[{}->{}]{:.4f}".format(int(rate * 100), a, b, loss), end="")
  print('')
  acc_val = check_accuracy(valLoader, model)
  running_loss /= len(trainingLoader)
  print(f'Epoch {epoch} training loss: {running_loss}')
end = time.time()
print(f'redis, batch size: {batch_size}, worker: {num_workers}')
print(f'end-to-end training time: {end - start}s')