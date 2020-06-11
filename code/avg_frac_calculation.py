import sys,os,glob
from statistics import mean

finput = sys.argv[1]
fout_dir = sys.argv[2]

fout = open(fout_dir+finput.split('/')[-1].split('.')[0]+"_avgMeth.txt",'w')
fout.write('chromosome\tposition\tHuman_meth\tChimp_meth\tMacaque_meth\n')

with open(finput,'r') as fp:
    for line in fp:
        line_temp = line.strip().split('\t')
        human_info,chimp_info,macaq_info = line_temp[3].split('..')
        human_M = str(round(mean([float(x.split('/')[0])/float(x.split('/')[1]) for x in human_info.split(',') if int(x.split('/')[1]) > 0 ]),3))
        chimp_M = str(round(mean([float(x.split('/')[0])/float(x.split('/')[1]) for x in chimp_info.split(',') if int(x.split('/')[1]) > 0 ]),3))
        macaq_M = str(round(mean([float(x.split('/')[0])/float(x.split('/')[1]) for x in macaq_info.split(',') if int(x.split('/')[1]) > 0 ]),3))
        fout.write(line_temp[0]+'\t'+line_temp[2]+'\t'+human_M+'\t'+chimp_M+'\t'+macaq_M+'\n')

fout.close()
