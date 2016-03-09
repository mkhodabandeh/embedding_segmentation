import h5py
import numpy as np
from scipy.io import savemat
import os.path

feat_path = '/cs/vml2/mkhodaba/datasets/VSB100/files/{}/features_8.npz'
similarities_path = '/cs/vml2/mkhodaba/datasets/VSB100/files/{}/similarities.mat'

def do(name):
    f = np.load(feat_path.format(name))
    features = [f['HOF'], f['FCN']]
    features = np.concatenate(features, axis=1)
    print features.shape
    if features.shape[0] > 12000:
        print 'feature dimension too high'
        return
    similarities = features.dot(features.T)
    savemat(similarities_path.format(name), {'similarities': similarities})

def main():
    with open('names.txt', 'r') as names:
        for name in names:
            name=name.strip()
            print 'video:', name
            if  not os.path.isfile(feat_path.format(name)):
                print 'Features not exist'
                continue
            do(name)
if __name__ == '__main__':
    main()
