import os
from mnist import MNIST
import pickle
import math

if __name__ == '__main__':

    raw = MNIST('./')

    images, labels = raw.load_training()

    granularity = 32

    object_dir = f'/home/mnist_objects_{granularity}'

    if not os.path.exists(object_dir):
        os.mkdir(object_dir)

    dataset_size = 60000
    object_num = int(math.ceil(dataset_size / granularity))
    i = 0
    while i < object_num:
        filename = "object" + str(i)
        sample = {}
        idxRange = [j for j in range(i * granularity, min(dataset_size, (i + 1) * granularity))]
        sample['img'] = [images[j] for j in idxRange]
        sample['label'] = [labels[j] for j in idxRange]

        with open(os.path.join(object_dir, filename), 'wb') as file:
            pickle.dump(sample, file)
            i += 1

