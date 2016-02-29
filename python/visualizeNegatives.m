function visualizeSimilars(sup, exp_num)
    
    exp_num = num2str(exp_num);
    folder_name = ['/cs/vml2/mkhodaba/eccv16/visualization/', exp_num,'-',num2str(sup), '-neg'];
    %load('/cs/vml3/mkhodaba/cvpr16/Graph_construction/Features/vw_commercial_vidinfo.mat')
    load('/cs/vml2/mkhodaba/datasets/VSB100/files/belly_dancing/voxellabelledlevelvideo_08.mat');
    %load('/cs/vml3/mkhodaba/cvpr16/Graph_construction/Features/STM_similarities.mat')
    %load('/cs/vml3/mkhodaba/cvpr16/Graph_construction/Features/anna_color_similarities.mat')
    %exp_root = '/cs/vml2/mkhodaba/cvpr16/expriments/';
    exp_root = '/local-scratch/expriments/';

    contents = dir(exp_root);
    contents = contents(3:end);
    contents = {contents.name};
    exp_num = contents{strncmpi(exp_num, contents, length(exp_num))};
    disp(exp_num);
    %assert(isa(exp_num,'string'));
    load([exp_root, exp_num ,'/similarities.mat']);        
    a = [exp_root, exp_num, '/indices.mat']
    load([exp_root, exp_num, '/indices.mat']);

    labelledelevelvideo= double(labelledlevelvideo);
    database_negative_indices = database_negative_indices + 1;
    database_neighbor_indices = database_neighbor_indices + 1;

    negatives = database_negative_indices(sup, :)
    negatives= zeros(1, size(similarities,1));
    negatives(database_negative_indices(sup, :)) = 1;

    neighbors = database_neighbor_indices(sup, :)
    neighbors= zeros(1, size(similarities,1));
    neighbors(database_neighbor_indices(sup, :)) = 1;
    %load([exp_root, exp_num ,'/refined_similarities.mat']);        
    %load('/cs/vml3/mkhodaba/cvpr16/Graph_construction/Features/allsegsvw_commercial.mat'])
    %similarities = -1 * similarities;
    mkdir(folder_name)
    row=similarities(sup,:);
    maxx=max(row)
    minx=min(row)
    labelledelevelvideo= double(labelledlevelvideo);
    SpringColors=spring(5002);
    seg10 = labelledlevelvideo(:,:,1);
    img_seg10 = double(cat(3,seg10,seg10,seg10));
    height = size(seg10,1)
    width = size(seg10, 2)
    
    for frame = 1:50
        current_frame_label=labelledlevelvideo(:,:,frame);
        %size(seg10)
        %type(labelledlevelvideo)
        for i = 1:height
            for j = 1:width
                sup_idx = current_frame_label(i,j);
                if sup_idx == sup
                    img_seg10(i,j,1)=0.1;
                    img_seg10(i,j,2)=0.1;
                    img_seg10(i,j,3)=1;
                elseif negatives(sup_idx) == 1
                    img_seg10(i,j,1)=1;
                    img_seg10(i,j,2)=0.1;
                    img_seg10(i,j,3)=0.1;
                elseif neighbors(sup_idx) == 1
                    img_seg10(i,j,1)=0.1;
                    img_seg10(i,j,2)=1;
                    img_seg10(i,j,3)=0.1;
                else
                    value=row(sup_idx);
                    value=ceil(5000*(value-minx)/(maxx-minx))+1;
                    img_seg10(i,j,1)=SpringColors(value,1);
                    img_seg10(i,j,2)=SpringColors(value,2);
                    img_seg10(i,j,3)=SpringColors(value,3);
                end
            end
        end
    imwrite(img_seg10,[folder_name, '/', num2str(frame), '.jpg']);
    end
end
%figure;
%histogram(row20);
