import numpy as np
import tarfile
import cPickle
import pickle
import os

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = cPickle.load(fo)
    return dict


def load_cifar_10_data(dir):

    images = np.empty((5, 10000, 3072), dtype=np.uint8)
    labels = np.empty((5, 10000), dtype=np.uint8)

    for i in range(5):
        file_name = '{}/data_batch_{}'.format(dir, i + 1)
        d = unpickle(file_name)
        images[i] = d['data']
        labels[i] = d['labels']

    images = images.reshape(50000, 3072).tolist()
    labels = labels.reshape(50000).tolist()
    
    print(type(images))
    
    
    return images, labels


if __name__ == "__main__":

    dir = './cifar-10-batches-py'

    images, labels = load_cifar_10_data(dir)
    
    object_dir = './cifar10_objects'
    
    i = 0
    while i < 50000: 
        filename = "img" + str(i)
        sample = {'img': images[i], 'label': labels[i]}
    
        with open(os.path.join(object_dir, filename), 'wb') as file:
            pickle.dump(sample, file)
            i += 1
    
    filename = "img4288"
    with open(os.path.join(object_dir, filename), 'rb') as fo:
        dict = pickle.loads(fo.read())
    
    print(dict)