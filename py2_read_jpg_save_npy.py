import glob
import numpy as np
import skimage.io as io

folder = 'data/BSR/BSDS500/data/images/test/'
images = glob.glob(folder + '*.jpg')
for filename in images:
    img = io.imread(filename)
    np.save(filename+'.npy', img)
