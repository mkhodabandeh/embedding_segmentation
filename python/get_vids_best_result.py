import glob
import sys, os

def getall(vidname):
    path = '/cs/vml2/mkhodaba/datasets/VSB100/results_new/{}/*.txt'.format(vidname)
    vpr = []
    bpr = []
    name = []
    for respath in glob.glob(path):
        with open(respath, 'r') as resfile:
            for i, line in enumerate(resfile):
                if i == 2:
                    bpr.append(float(line[31:36]))
                if i == 6:
                    vpr.append(float(line[31:36]))
                    name.append(os.path.basename(respath))
                    break
    return vpr, bpr, name

def getmax(vidname):
    cum_vpr, cum_bpr = 0,0
    num = 0 
    for i in xrange(10):
        if os.path.isdir('/cs/vml2/mkhodaba/datasets/VSB100/results_new/'+vidname+str(i)):
            vpr, bpr, _ = getall(vidname+str(i))
            if vpr:
                index = vpr.index(max(vpr))
                cum_vpr+= vpr[index] 
                cum_bpr+= bpr[index] 
                num+=1
            else:
                print 'Empty1:', vidname
    if num == 0:
        print 'EMPTY:', vidname
        return None, None
    vpr = cum_vpr*1.0/num

    bpr = cum_bpr*1.0/num
    return vpr, bpr 

if __name__ == '__main__':
    argv = sys.argv
    vpr, bpr = [],[]
    anames = []
    if '-v' not in argv:
        with open('/cs/vml3/mkhodaba/cvpr16/code/embedding_segmentation/python/names.txt') as names:
            for name in names:
                name = name.strip()
                vpr_temp, bpr_temp = getmax(name)
                if vpr_temp:
                    vpr.append(vpr_temp)
                    bpr.append(bpr_temp)
                    anames.append(name)
        arr = zip(anames, zip(vpr,bpr))
        arr.sort(key=lambda x: x[1][0])
        print '\n'.join( map(lambda x: 'Video: {}\nVpr:{}, Bpr:{}\n'.format(x[0], x[1][0], x[1][1]), arr))

        print sum(vpr)/len(vpr)
        print 'number of videos:', len(vpr)
        exit()
    v = argv.index('-v')
    vidname = argv[v+1]
    print vidname
    try:
        if '-a' in argv:
            vpr, bpr, name = getall(vidname)
        else:
            vpr, bpr, name = getmax(vidname)

        if vpr is not None:
            for i in xrange(len(vpr)):
                print 'BPR:{0:.2f}\nVPR:{1:.2f}\n{2}\n'.format(bpr[i], vpr[i], name[i])
                # print 'VPR: {0}\n{2}\n'.format(int(vpr*100), bpr, name)
    except:
        print 
