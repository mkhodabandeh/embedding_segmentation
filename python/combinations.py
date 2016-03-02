from multiprocessing import Pool
import os


def run_command(cmd):
    print cmd
    os.system(cmd)
    return cmd

machine = 'cs-vml-05'
parameters = {
        # '-v': ['airplane', 'rock_climbing', 'new_york', 'yosemite', 'chameleons', 'arctic_kayak', 'animal_chase', 'ballet', 'planet_earth_2', 'planet_earth_1'],
        '-v': ['planet_earth_2', 'planet_earth_1'],
        # '-b': [128],
        # '-a': [12],
        # '-A': [4],
        # '-S': [400],
        # '-o': [128],
        # '-l': [3]
        '-b': [256],
        '-a': [8, 12],
        '-A': [6],
        '-S': [400, 800, 1500],
        # '-o': [64, 128, 256],
        # '-l': [3]
        }

log_path = '/cs/vml2/mkhodaba/cvpr16/logs/{}/'.format(machine)
os.system('mkdir {} -p'.format(log_path))
proj_path = '/cs/vml3/mkhodaba/cvpr16/code/embedding_segmentation/python/'
def dfs(i, params_list, cmd, processes):
    if i == len(params_list):
        params_str = ' '.join(map(str, cmd))
        comment_str = '_'.join(map(str, cmd)).replace('-', '')
        # processes.append('python {0}/exec_scripts.py {1} -c {2} -f > {3}/exp_{2}.log 2>&1'.format(proj_path,params_str, comment_str, log_path))
        processes.append('python {0}/exec_scripts.py {1} -c {2} -f'.format(proj_path,params_str, comment_str))
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
    start = 1
    for i,cmd in enumerate(processes_list):
        # print cmd
        run_command(cmd)
        print 'khoreva ', start+i
        os.system('python '+proj_path+'/run_khoreva.py '+str(start+i))
        
    # start = 1 
    # for i in xrange(len(params_list)):
        # os.system('python '+proj_path+'/run_khoreva.py '+str(start+i))

if __name__ == '__main__':
    main()


