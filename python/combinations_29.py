from multiprocessing import Pool
import os


def run_command(cmd):
    print cmd
    os.system(cmd)
    return cmd

start = 1 
machine = 'cs-vml-29'
videos = ['birds_of_paradise', 'koala', 'fisheye', 'street_food', 'airplane', 'jungle_cat']
parameters = {
        # '-v':['baseball', 'beach_volleyball', 'belly_dancing', 'beyonce', 'bicycle_race', 'birds_of_paradise', 'buck', 'buffalos', 'capoeira', 'fisheye', 'fish_underwater'],
        '-v':[]  ,
        # '-b': [128],
        # '-a': [12],
        # '-A': [4],
        # '-S': [400],
        # '-o': [128],
        # '-l': [3]
        '-b': [256],
        '-a': [4],
        '-A': [2],
        '-S': [400],
        '-o': [256],
        '-l': [8],
        '-B': [16,32],
        # '-o': [64, 128, 256],
        # '-l': [3]
        }

for vid in videos:
    for i in xrange(0, 10):
        if os.path.isdir('/local-scratch/segmented_frames/{}{}'.format(vid,i)):
            parameters['-v'].append('{}{}'.format(vid, i))

print parameters
log_path = '/cs/vml2/mkhodaba/cvpr16/logs/{}/'.format(machine)
os.system('mkdir {} -p'.format(log_path))
proj_path = '/cs/vml3/mkhodaba/cvpr16/code/embedding_segmentation/python/'
def dfs(i, params_list, cmd, processes):
    if i == len(params_list):
        params_str = ' '.join(map(str, cmd))
        comment_str = '_'.join(map(str, cmd)).replace('-', '')
        processes.append('python {0}/exec_scripts.py {1} -c {2} -f  > {3}/exp_{2}_{4}.log 2>&1'.format(proj_path,params_str, comment_str, log_path, machine))
        # processes.append('python {0}/exec_scripts.py {1} -c {2} -f'.format(proj_path,params_str, comment_str))
    else:
        for p in params_list[i][1]:
            cmd.append(params_list[i][0])
            cmd.append(p)
            dfs(i+1, params_list, cmd, processes)
            cmd.pop()
            cmd.pop()
def main():
    params_list = list(parameters.iteritems())
    matlab_list = []
    processes_list = []
    dfs(0, params_list, [], processes_list)
    # print '\n'.join(processes_list)

    runner_par = run_command
    # pool = Pool()
    # pool.map(runner_par, processes_list)
    # pool.close()
    # pool.join()
    for i,cmd in enumerate(processes_list):
        # print cmd
        run_command(cmd)
        # print 'khoreva ', start+i
        # pass
        os.system('python '+proj_path+'/run_khoreva.py ')
        
    # for i in xrange(len(processes_list)):
        # os.system('python '+proj_path+'/run_khoreva.py '+str(start+i))

if __name__ == '__main__':
    main()


