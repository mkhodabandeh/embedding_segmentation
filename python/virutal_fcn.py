import os
import glob
from multiprocessing import Pool

fcn_path = '/cs/vml2/smuralid/projects/eccv16/python/preprocessing/fcn/Test/'
dest_path = '/cs/vml1/users/mkhodaba/fcn/'


def getGT(name):
    gt_path = '/cs/vml2/mkhodaba/datasets/VSB100/General_test_fullres/Groundtruth/{}/*.mat'.format(name)
    gts = [int(os.path.basename(x)[5:8]) for x in glob.glob(gt_path)]
    num_frames = len(glob.glob(fcn_path+name+'/*.npz'))
    start = gts[0]
    return num_frames, start, gts

flag = False
def do(name):
    name = name.strip()
    print 'video:', name
    num_frames, start, gts = getGT(name)
    is_dir =  os.path.isdir('/local-scratch/segmented_frames/'+name)
    print ' gts:',gts, ' start:',start, ' num_frames:', num_frames
    for i,gt_num in enumerate(gts):
        # os.system('rm -rf '+frame_path+name+str(i))
        # os.system('rm -rf '+flow_path+name+str(i))
        os.system('mkdir '+dest_path+name+str(i)+' -p')
        s = max(start, gt_num-10)
        e = min(num_frames+start, gt_num+10)
        print i, gt_num, ' frames:', s, '-',e

        for sh,fnum in enumerate(xrange(s-start+1, e-start+1)):
            # print fnum, type(fnum)
            j = sh+1
            os.system('cp /{0}/{1}/{2:05d}.npz '.format(fcn_path, name, fnum)+\
                        ' /{0}/{1}/{2:05d}.npz'.format(dest_path, name+str(i), j))
            # os.system('cp /{0}/{1}/{2:05d}.ppm '.format(flow_path, name, fnum)+\
                        # ' /{0}/{1}/{2:05d}.ppm'.format(flow_path,name+str(i),j))
            # if is_dir: 
                # for lvl in xrange(11):
                    # os.system('mkdir /local-scratch/segmented_frames/{0}/{1:02d} -p'.format(name+str(i), lvl))
                    # os.system('cp /local-scratch/segmented_frames/{0}/{1:02d}/{2:05d}.ppm '.format(name, lvl, fnum)+\
                            # ' /local-scratch/segmented_frames/{0}/{1:02d}/{2:05d}.ppm'.format(name+str(i),lvl, j))
def main(names):
    pool = Pool()
    pool.map(do, names)
    pool.close()
    pool.join()

if __name__=='__main__':
    import sys
    start = int(sys.argv[1])
    f = open('names.txt', 'r')
    names = [x.strip() for x in f] 

    main(names[start:min(len(names), start+8)])

# for i, vid in enumerate(glob.glob('/local-scratch/segmented_frames/*')):
