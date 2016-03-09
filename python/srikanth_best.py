import glob
import sys, os
def getall(vidname):
    path = '/cs/vml2/smuralid/projects/eccv16/dataset/VSB100/results/{}/*.txt'.format(vidname)
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
    if '-v' not in argv:
        raise
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
