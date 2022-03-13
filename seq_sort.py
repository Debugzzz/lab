infile_path = input("Please input the infile_path:")
outfile_path = input("Please input the outfile_path:")

mes0 = open(infile_path,'r')
mes1 = open(outfile_path,'w+')

lines = mes0.readlines()
lines_sorted = sorted(lines)


for line in lines_sorted:
    mes1.write(line)

mes0.close()
mes1.close()
