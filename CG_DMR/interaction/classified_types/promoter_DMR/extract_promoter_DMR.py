import sys,glob
import os
flist = glob.glob("../info/H*_info.txt")
for sfile in flist:
    systemstr = "bedtools intersect -a "+sfile+" -b PR_ortho.bed -f 0.5 -wb | cut -f 1,2,3,31 > "+sfile.split('/')[-1].replace('_info.txt','_PR_DMR_gene.txt')
    print (systemstr)
    os.system(systemstr)
