import h5py
import numpy as np
import sys
from PIL import Image

num_cats = int(sys.argv[1])
num_dogs = int(sys.argv[2])

num_examples = num_cats + num_dogs
train_x = np.zeros((num_examples, 200, 200, 3))
train_y = np.zeros((1, num_examples))

for i in xrange(num_cats):
    img = Image.open('normalized/train/cat.' + str(i) + '.jpg')
    pix = img.load()
    size = img.size
    for x in xrange(size[0]):
        for y in xrange(size[1]):
            r, g, b = pix[x, y]
            train_x[i][x][y] = [r, g, b]

    if i % 100 == 0:
        print 'cat ', i, ' done'
    train_y[0][i] = 1
            
for i in xrange(num_dogs):
    img = Image.open('normalized/train/dog.' + str(i) + '.jpg')
    pix = img.load()
    size = img.size
    for x in xrange(size[0]):
        for y in xrange(size[1]):
            r, g, b = pix[x, y]
            train_x[num_cats + i][x][y] = [r, g, b]
            
    if i % 100 == 0:
        print 'dog ', i, ' done'
    train_y[0][num_cats + i] = 0

hf = h5py.File('train.h5', 'w')
hf.create_dataset('dataset_x', data=train_x)
hf.create_dataset('dataset_y', data=train_y)
hf.close()

