import os
from mnist import MNIST
import pickle

if __name__ == '__main__':


    object_dir = './mnist_objects'
    raw = MNIST('./')

    images, labels = raw.load_training()

    i = 0
    while i < 60000: 
        filename = "img" + str(i)
        sample = {'img': images[i], 'label': labels[i]}
    
        with open(os.path.join(object_dir, filename), 'wb') as file:
            pickle.dump(sample, file)
            i += 1