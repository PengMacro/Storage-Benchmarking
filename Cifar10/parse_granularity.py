import numpy as np
import tarfile
import pickle
import os
import math

def unpickle(file):
    with open(file, 'rb') as fo:
        batchDict = pickle.load(fo, encoding ='latin1')
    return batchDict


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

    #print(type(images))


    return images, labels


if __name__ == "__main__":

    dir = './cifar-10-batches-py'

    granularity = 50000
    dataset_size = 50000
    object_num = int(math.ceil(dataset_size / granularity))

    images, labels = load_cifar_10_data(dir)

    if not os.path.exists(f'./cifar10_objects_{granularity}'):
        os.mkdir(f'./cifar10_objects_{granularity}')
    object_dir = f'./cifar10_objects_{granularity}'

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

    filename = "object0"
    with open(os.path.join(object_dir, filename), 'rb') as fo:
        dict = pickle.loads(fo.read())

    #print(dict)