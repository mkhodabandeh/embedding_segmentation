function run_all(experiment_name, level, video_name)
    addpath(genpath('/cs/vml3/mkhodaba/cvpr16/code/Graph_construction/'));
    VSS(video_name,'ucm2level',level,'uselevelfrw', '1', 'ucm2levelfrw', level, 'newmethodfrw', '1', 'stpcas', 'paperoptnrm', 'experiment', experiment_name);
    validate(experiment_name);

end
 

