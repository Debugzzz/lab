import os                                               #导入os模块
print("This is a seq_remove_duplicate program.")
lines_seen = set()                                      #创建不重复元素集
infilename = input("Please input the in_file_name:")    #接受输入
outfilename = input("Please input the out_file_name:")

infile = open(infilename,'r')
outfile = open(outfilename,'w+')

for line in infile:
    if line not in lines_seen:
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
infile.close()
