import h5py
import numpy as np
import sys
from PIL import Image

num_tests = int(sys.argv[1])

train_x = np.zeros((num_tests, 200, 200, 3))
train_y = np.zeros((1, num_tests))

for i in xrange(num_tests):
    img = Image.open('normalized/test1/' + str(i) + '.jpg')
    pix = img.load()
    size = img.size
    for x in xrange(size[0]):
        for y in xrange(size[1]):
            r, g, b = pix[x, y]
            train_x[i][x][y] = [r, g, b]

            
train_y = [1, 0, 0, 0, 0, 1, 1, 1, 1, 1]
train_y.extend([1, 1, 0, 1, 1, 1, 1, 0, 0, 1])
train_y.extend([1, 0, 1, 0, 0, 1, 0, 0, 1, 1])
hf = h5py.File('test1.h5', 'w')
hf.create_dataset('dataset_x', data=train_x)
hf.create_dataset('dataset_y', data=train_y)
hf.close()

