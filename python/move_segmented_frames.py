import os
import glob

frame_path = '/cs/vml2/mkhodaba/datasets/VSB100/Test/'
flow_path = '/cs/vml2/mkhodaba/datasets/VSB100/Test_flow/'


def getGT(name):
    gt_path = '/cs/vml2/mkhodaba/datasets/VSB100/General_test_fullres/Groundtruth/{}/*.mat'.format(name)
    gts = [int(os.path.basename(x)[5:8]) for x in glob.glob(gt_path)]
    num_frames = len(glob.glob(frame_path+name+'/ppm/*.ppm'))
    start = gts[0]
    return num_frames, start, gts

with open('names.txt', 'r') as names:
    for name in names:
        name = name.strip()
        is_dir =  os.path.isdir('/local-scratch/segmented_frames/'+name)
        if not is_dir:
            continue
        num_frames, start, gts = getGT(name)
        print 'video:', name
        print ' gts:',gts, ' start:',start, ' num_frames:', num_frames
        for i,gt_num in enumerate(gts):
            # os.system('rm -rf '+frame_path+name+str(i))
            # os.system('rm -rf '+flow_path+name+str(i))
            # os.system('mkdir '+frame_path+name+str(i)+'/ppm -p')
            # os.system('mkdir '+flow_path+name+str(i)+'/ -p')
            s = max(start, gt_num-10)
            e = min(num_frames+start, gt_num+10)
            print i, gt_num, ' frames:', s, '-',e

            for lvl in xrange(11):
                os.system('mkdir /local-scratch/segmented_frames/{0}/{1:02d} -p'.format(name+str(i), lvl))
                        ' /local-scratch/segmented_frames/{0}/{1:02d}/{2:05d}.ppm'.format(name+str(i),lvl, j))
                for sh,fnum in enumerate(xrange(s-start+1, e-start+1)):
                    j = sh+1
                    os.system('cp /local-scratch/segmented_frames/{0}/{1:02d}/{2:05d}.ppm '.format(name, lvl, fnum)+\

    os.system('bash /cs/vml2/mkhodaba/give_permission.sh')
# for i, vid in enumerate(glob.glob('/local-scratch/segmented_frames/*')):
