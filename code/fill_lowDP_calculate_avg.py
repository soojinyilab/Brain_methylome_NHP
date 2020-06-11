import sys
import numpy as np

finput = sys.argv[1]
fout   = open(sys.argv[1].replace('/2_merged_excluding_lowDP_cytosine_report/','/3_merged_fractional_cytosine_report/').replace('.excSNP.DP.bed','.excSNP.DP.frac.bed'),'w')
meth_level = {0:0,0.2:0,0.4:0,0.6:0,0.8:0}

with open(finput,'r') as fp:
    for line in fp:
        line_temp = line.strip().split('\t')
        methyl = line_temp[-1].split(',')
        valid_samples_avg = str(round(np.mean([float(x.split('/')[0])/float(x.split('/')[1]) for x in methyl if int(x.split('/')[-1]) >=5]),4))
        new_methyl = [str(round(float(x.split('/')[0])/float(x.split('/')[1]),4)) if int(x.split('/')[-1]) >= 5 else valid_samples_avg for x in methyl]
        fout.write('\t'.join(line_temp[0:-1])+'\t'+','.join(new_methyl)+'\n')
        avg_meth =  float(valid_samples_avg)
        if avg_meth < 0.2:
            meth_level[0] +=1
        elif avg_meth >= 0.2 and avg_meth < 0.4:
            meth_level[0.2] +=1
        elif avg_meth >= 0.4 and avg_meth < 0.6:
            meth_level[0.4] +=1
        elif avg_meth >= 0.6 and avg_meth < 0.8:
            meth_level[0.6] +=1
        elif avg_meth >= 0.8 and avg_meth <= 1:
            meth_level[0.8] +=1
              
fout2 = open('summary_log/summary_'+sys.argv[1].split('/')[-1]+".txt",'w')
for i in [0,0.2,0.4,0.6,0.8]:
    fout2.write(str(i)+'\t'+str(meth_level[i])+'\n')
fout2.close()
fout.close()

