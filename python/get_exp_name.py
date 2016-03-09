from configs import *
import sys

if len(sys.argv) == 1: 
    conf = getConfigs(-1) 
else: 
    conf = getConfigs(int(sys.argv[1])) 
try:
    print conf.experiment_folder_name
except:
    if conf.comment:
            conf.experiment_folder_name = '{0}-{1}'.format(conf.experiment_number,conf.comment)
    else:
        conf.experiment_folder_name = '{0}'.format(conf.experiment_number)
    print conf.experiment_folder_name
