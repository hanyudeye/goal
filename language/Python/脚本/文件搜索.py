# 遍历搜索位置下的每一个文件夹，并将指定类型文件复制到输出位置

import os
import shutil
#确定搜索的位置
dir_origin = r"D:\\test_orgin\\"
#确定搜索到的文件的输出位置
dir_target = r"D:\\test\\"
#选择搜索的文件类型
type_select = '文档' 
file_type = {'文档':['.doc','.docx','.wps','.txt','.rtf'],
             '表格':['.xls','.xlsx','.csv','.xlsm'],
             '压缩包':['.rar','.zip','.arj','.gz','.z'],
             'PDF':['.pdf'],
             '图片':['.jpg','.png','.bmp','.gif','.pic','.tif'],
             '音频':['.wav','.aif','.au','.mp3','.ram'],
             '视频':['.avi','.mpg','.mov','.swf']}
         
for root, dirs, files in os.walk(dir_origin):
    for file in files:
        if os.path.splitext(file)[-1] in file_type[type_select]:
            current_file = os.path.join(root, file)
            print(current_file)
            shutil.copy(current_file, dir_target)