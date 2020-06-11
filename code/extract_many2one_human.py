import sys

finputs = sys.argv[1]
ftarget = sys.argv[2]
out_dir = sys.argv[3]
dd = {}
with open(ftarget,'r') as fp:
    for line in fp:
        dd[line.strip()] = ''
fout = open(out_dir+finputs.split('/')[-1],'w')
with open(finputs,'r') as fp:
    for line in fp:
        with open(line.strip(),'r') as fp2:
            for line2 in fp2:
                line_temp2 = line2.strip().split('\t')
                if line_temp2[-1] in dd:
                    fout.write(line2)
fout.close()
