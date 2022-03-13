#This is a python program.
import os
filedir = input("Please input the dir_path:")              #目标文件夹路径
fileoutname = input("Please input the output_filename:")   #获取输出文件名
filenames = os.listdir(filedir)                            #获取目标文件夹中文件名称列表
print(filenames)                                           #输出目标文件夹中的文件名称
print(len(filenames))                                      #输出目标文件夹中文件个数

f = open(fileoutname,'w+')                                 #新建输出文件

for filename in filenames:                                 #遍历文件名
    filepath = filedir + '/' + filename                    #构建文件路径
    for line in open(filepath):                            #遍历单个文件，读取文件行
        f.writelines(line)                                 #将文件行写入输出文件
    f.write('\n')                                          #在一个文件输出完成后添加换行符

f.close()
