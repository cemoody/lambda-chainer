import os
import ctypes
import six

for d, dirs, files in os.walk('lib'):
    for f in files:
        if f.endswith('.a'):
            continue
        ctypes.cdll.LoadLibrary(os.path.join(d, f))

import sklearn
import chainer
import pandas


import numpy as np
from PIL import Image

import chainer
from chainer import cuda
import chainer.functions as F
from chainer.links import caffe

print('Downloading ILSVRC12 mean file for NumPy...')
six.moves.urllib.request.urlretrieve(
    'https://github.com/BVLC/caffe/raw/master/python/caffe/imagenet/'
    'ilsvrc_2012_mean.npy',
    'ilsvrc_2012_mean.npy')

print('Downloading NIN model file for NumPy...')
url = 'https://dl.dropboxusercontent.com/u/206140/'
name = 'nin_imagenet.caffemodel'
six.moves.urllib.request.urlretrieve(url, name)
import urllib2
fh = urllib2.urlopen(url + name)
with open(name, 'wb') as output:
  output.write(fh.read())

xp = np

func = caffe.CaffeFunction(name)

def handler(event, context):
    # do sklearn stuff here
    mean_image = np.ndarray((1, 3, 256, 256), dtype=np.float32)
    mean_image[:, 0, :, :] = 104
    mean_image[:, 1, :, :] = 117
    mean_image[:, 2, :, :] = 123
    y, = func(inputs={'data': mean_image}, outputs=['pool4'], train=False)
    return {'yay': y.data}

print(handler({}, {}))
