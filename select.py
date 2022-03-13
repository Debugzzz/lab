fasfile = input("Please input the fasta_file:")
infile = input("Please input the infile:")
outfile = input("Please input the outfile:")

seq_file = open(fasfile)
seq = {}
for line in seq_file:
    if line.startswith('>'):
        name=line
        seq[name]=''
    else:
        seq[name]+=line.replace('\n','').strip()
seq_file.close()

testseq = open(infile)
out = open(outfile,'w')

for i in testseq:
    for gene,sequence in seq.items():
        if i == gene:
            out.write(gene)
            out.write(sequence + '\n')
        else:
            continue

testseq.close()
out.close()
