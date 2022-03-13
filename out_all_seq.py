print("This is a out_all_seq program.(from blast result file)")
input_file_name = input("Please input the input_file_name:")
output_file_name = input("Please input the output_file_name:")
f_name = open(input_file_name,'r')
f_out = open(output_file_name,'w+')
line = f_name.readlines()

for i in line:
    if ">" in i:
        print(i)
        f_out.write(i)
f_out.close()
f_name.close()
