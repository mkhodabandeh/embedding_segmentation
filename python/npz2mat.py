import numpy as np
from scipy.io import savemat
import sys

spath = sys.argv[1]
dpath = sys.argv[2]

a = np.load(spath)
savemat(dpath, a)
