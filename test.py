import os
import ctypes
import six
import json
import time

for d, dirs, files in os.walk('lib'):
    for f in files:
        if f.endswith('.a'):
            continue
        ctypes.cdll.LoadLibrary(os.path.join(d, f))

import chainer


import numpy as np
from PIL import Image

import chainer
from chainer import cuda
import chainer.functions as F
from chainer.links import caffe

print('Downloading NIN model file for NumPy...')
url = 'https://dl.dropboxusercontent.com/u/206140/'
name = 'nin_imagenet.caffemodel'
import urllib2
fh = urllib2.urlopen(url + name)
with open('/tmp/' + name, 'wb') as output:
  output.write(fh.read())

xp = np

func = caffe.CaffeFunction('/tmp/' + name)

def handler(event, context):
    # do sklearn stuff here
    mean_image = np.ndarray((1, 3, 256, 256), dtype=np.float32)
    mean_image[:, 0, :, :] = 104
    mean_image[:, 1, :, :] = 117
    mean_image[:, 2, :, :] = 123
    y, = func(inputs={'data': mean_image}, outputs=['pool4'], train=False)
    ret = json.dumps(len(y.data.tolist()))
    return {'yay': ret}

t0 = time.time()
print(handler({}, {}))
t1 = time.time()
print(t1 - t0)
