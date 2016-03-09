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
    vpr, bpr, name = getall(vidname)
    i = vpr.index(max(vpr))
    return [vpr[i]], [bpr[i]], [name[i]]

if __name__ == '__main__':
    argv = sys.argv
    vpr, bpr = [],[]
    names = []
    if '-v' not in argv:
        for v in glob.glob('/cs/vml2/mkhodaba/datasets/VSB100/results_new/*'):
            v = os.path.basename(v)
            # print v
            try:
                vpr_temp, bpr_temp, name_temp = getmax(v)
                if vpr_temp:
                    # print bpr_temp[0], vpr_temp[0], '\n'
                    vpr.append(vpr_temp[0])
                    bpr.append(bpr_temp[0])
                    names.append(v)
            except:
                print v, '-> empty'
        # print len(vpr)
        # print 'VPR:', sum(vpr)/len(vpr)
        # print 'BPR:', sum(bpr)/len(bpr)
        
        arr = zip(names, zip(vpr,bpr))
        arr.sort(key=lambda x: x[0])
        print '\n'.join( map(lambda x: 'Video: {}\nVpr:{}, Bpr:{}\n'.format(x[0], x[1][0], x[1][1]), arr))

        print sum(vpr)/len(vpr)
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
