import sys,os,glob
from statistics import mean

finput = sys.argv[1]
fout_dir = '/'.join(sys.argv[1].split('/')[0:-1])+'/remain_PCA_informative/'

fout = open(fout_dir+finput.split('/')[-1].replace('_Meth.txt','_Meth.PCA.txt'),'w')

with open(finput,'r') as fp:
    stitle = fp.readline().strip().split('\t')
    fout.write('loci\t'+'\t'.join(stitle[2:])+'\n')
    sam_size = len(stitle) - 2
    for line in fp:
        temp_parse = line.strip().split('\t')
        tmp_loci,line_temp = '_'.join(temp_parse[0:2]),temp_parse[2:]
        meth_indi = [float(x) for x in line_temp]
        cnt_too_high = sum(i >= 0.9  for i in meth_indi)
        cnt_too_low  = sum(i <= 0.1  for i in meth_indi)
        if float(cnt_too_high) > (float(sam_size)*0.9) or float(cnt_too_low) > (float(sam_size)*0.9):
            continue
        '''
        human_ND_info,chimp_ND_info,macaq_ND_info,human_OD_info,chimp_OD_info,macaq_OD_info =line_temp[0:10],line_temp[10:20],line_temp[20:30],line_temp[30:40],line_temp[40:50],line_temp[50:60]
        human_ND_M = mean([float(x) for x in human_ND_info ])
        chimp_ND_M = mean([float(x) for x in chimp_ND_info ])
        macaq_ND_M = mean([float(x) for x in macaq_ND_info ])
        human_OD_M = mean([float(x) for x in human_OD_info ])
        chimp_OD_M = mean([float(x) for x in chimp_OD_info ])
        macaq_OD_M = mean([float(x) for x in macaq_OD_info ])
        
        if human_ND_M > 0.9 and chimp_ND_M > 0.9 and macaq_ND_M > 0.9 and human_OD_M > 0.9 and chimp_OD_M > 0.9 and macaq_OD_M > 0.9:
            continue
        if human_ND_M < 0.1 and chimp_ND_M < 0.1 and macaq_ND_M < 0.1 and human_OD_M < 0.1 and chimp_OD_M < 0.1 and macaq_OD_M < 0.1:
            continue
        '''
        fout.write(tmp_loci+'\t'+'\t'.join(line_temp)+'\n')

fout.close()


'''
AN05483_Control_NeuN	X1525_Control_NeuN	X1527_Control_NeuN	X1531_Control_NeuN	X1536_Control_NeuN	X1538_Control_NeuN	X1539_Control_NeuN	X3590_Control_NeuN	X3602_Con
trol_NeuN	X4615_Control_NeuN	ABBY_ND	ANJA_ND	BELEKA_ND	CALLIE_ND	DUNCAN_ND	LULU_ND	LYK_ND	MELISSA_ND	OSSABAW_ND	Roger_ND	YN04-200_ND	YN08-380_ND	Y
N09-122_ND	YN09-173_ND	YN09-179_ND	YN09-72_ND	YN11-64_ND	YN11-77_ND	YN12-654_ND	YN14-248_ND	AN03398_Control_Olig2	AN15240_Control_Olig2	AN16799_Control_Olig2	X
1527_Control_Olig2	X1532_Control_Olig2	X1538_Control_Olig2	X1539_Control_Olig2	X1541_Control_Olig2	X3602_Control_Olig2	X4615_Control_Olig2	ABBY_OD	ANJA_OD	BELEKA_OD	B
JORN_OD	CALLIE_OD	DUNCAN_OD	LULU_OD	MELISSA_OD	OSSABAW_OD	Roger_OD	YN04-200_OD	YN08-380_OD	YN09-122_OD	YN09-173_OD	YN09-72_OD	YN11-300_OD	YN11-77_O
D	YN11-78_OD	YN12-654_OD	YN14-248_OD
1.00000	0.95238	0.92000	0.90323	0.91304	0.96154	0.90476	0.95652	0.85714	0.88889	1.00000	0.66667	1.00000	1.00000	0.90000	1.00000	1.00000	0.88889	1.00000	0.80000	1.00000	0.92857	0.93333	1.00000	1.00000	0
.93333	0.85714	1.00000	1.00000	0.92308	0.64706	0.83333	0.77778	0.77143	0.84848	0.92593	0.73077	0.85000	0.93548	0.92308	1.00000	1.00000	1.00000	0.50000	0.57143	0.88889	1.00000	0.71429	1.00000	1.00000	0
.95000	0.81818	0.80000	0.80000	0.88462	1.00000	0.81818	0.80000	0.88889	0.92857
0.92000	0.95238	0.91667	1.00000	0.94737	0.95652	1.00000	0.96000	1.00000	1.00000	1.00000	1.00000	1.00000	1.00000	1.00000	1.00000	1.00000	0.94444	1.00000	1.00000	0.93750	1.00000	0.92857	0.92308	1.00000	1
.00000	1.00000	0.91667	1.00000	1.00000	0.93750	1.00000	0.92857	0.92857	0.94118	0.93103	0.96000	0.95455	0.86207	0.92857	1.00000	1.00000	0.80000	1.00000	0.90000	1.00000	1.00000	1.00000	1.00000	1.00000	0
.95238	0.91304	0.96296	1.00000	0.88000	0.94118	0.95000	0.86364	1.00000	1.00000
1.00000	0.95455	0.94444	1.00000	1.00000	1.00000	1.00000	0.95455	1.00000	1.00000	0.90909	0.00000	1.00000	0.88889	1.00000	0.50000	1.00000	1.00000	1.00000	1.00000	0.85714	0.88889	1.00000	0.85714	1.00000	1
.00000	1.00000	0.94118	1.00000	0.85714	1.00000	0.89474	0.94737	1.00000	0.94444	0.95652	1.00000	1.00000	1.00000	1.00000	0.75000	1.00000	0.85714	1.00000	1.00000	0.92857	0.25000	0.95238	1.00000	1.00000	1
.00000	0.86667	0.96552	0.92308	0.87500	0.80000	0.80952	0.92308	0.87500	0.94118
0.91667	0.95652	0.95652	0.90909	0.94444	0.95455	0.91304	0.92308	0.90476	0.96667	1.00000	1.00000	1.00000	1.00000	0.92308	0.80000	1.00000	0.94737	1.00000	0.90000	1.00000	1.00000	1.00000	1.00000	1.00000	0
.94118	0.93333	0.91667	0.94118	0.92308	0.66667	0.68966	0.76000	0.70000	0.81818	0.83333	0.53846	0.95238	0.79310	0.53333	0.87500	1.00000	0.75000	1.00000	0.72727	0.81818	1.00000	0.78261	0.50000	1.00000	0
.65000	0.80769	0.70370	0.63636	0.69231	0.84211	0.85000	0.77273	0.80000	0.86667
0.92308	0.95455	0.89474	0.95000	0.95833	1.00000	0.91667	0.95455	1.00000	0.87500	0.71429	1.00000	0.70000	0.80000	0.84615	0.50000	0.85714	1.00000	1.00000	1.00000	1.00000	1.00000	1.00000	1.00000	1.00000	0
.85000	0.92857	0.89474	1.00000	1.00000	0.82353	0.71429	0.80000	0.86364	1.00000	0.81818	0.50000	0.61111	0.86667	0.80000	0.55556	1.00000	0.62500	1.00000	0.88889	0.81250	0.50000	0.75000	1.00000	0.88889	0
.90909	0.81250	0.83333	0.86667	0.68750	0.57143	0.77273	0.83333	0.83333	0.62500
0.91667	0.95238	0.95238	1.00000	1.00000	0.90909	0.95833	1.00000	1.00000	1.00000	1.00000	1.00000	1.00000	0.92857	1.00000	1.00000	1.00000	1.00000	1.00000	1.00000	1.00000	0.93750	0.87500	1.00000	1.00000	1
.00000	0.93333	1.00000	1.00000	0.90909	0.86667	0.93333	0.84000	0.85714	0.93939	1.00000	0.88462	1.00000	0.93103	0.93750	1.00000	1.00000	1.00000	1.00000	1.00000	0.91667	1.00000	1.00000	1.00000	1.00000	0
.90476	0.84615	0.96429	0.81818	0.80769	0.89474	0.85714	0.81818	0.63158	0.84615
1.00000	1.00000	0.94118	1.00000	0.90909	1.00000	0.92857	1.00000	0.94444	1.00000	1.00000	1.00000	1.00000	0.91667	1.00000	1.00000	1.00000	0.93333	0.85714	1.00000	1.00000	1.00000	1.00000	1.00000	0.92857	1
.00000	1.00000	1.00000	0.81818	1.00000	0.94118	0.76190	0.90000	0.95455	0.87500	0.90909	0.89474	1.00000	1.00000	0.94118	0.90000	1.00000	1.00000	1.00000	1.00000	0.87500	0.40000	0.92857	1.00000	1.00000	0
.81818	0.86667	0.93333	0.92857	0.76471	0.68182	0.86364	0.84615	0.78261	0.81250
0.92857	0.94737	1.00000	0.92308	0.92857	1.00000	1.00000	1.00000	0.95000	1.00000	0.88889	0.90000	1.00000	1.00000	0.97436	1.00000	1.00000	0.96154	0.92857	0.94118	1.00000	0.81818	1.00000	1.00000	1.00000	1
.00000	0.95833	1.00000	0.90000	1.00000	0.90909	1.00000	0.90000	1.00000	0.92308	0.93333	0.93333	1.00000	0.90000	1.00000	0.93333	1.00000	1.00000	1.00000	0.92308	1.00000	0.90000	0.84444	1.00000	0.96154	0
.94118	0.92000	0.92308	0.92308	1.00000	1.00000	0.88889	1.00000	0.90000	0.88889
1.00000	1.00000	1.00000	1.00000	1.00000	1.00000	1.00000	1.00000	1.00000	1.00000	1.00000	1.00000	0.96000	1.00000	0.92000	1.00000	1.00000	0.90909	1.00000	0.94118	1.00000	1.00000	0.75000	1.00000	1.00000	0
.96296	1.00000	1.00000	1.00000	1.00000	1.00000	0.94118	0.94737	0.93333	1.00000	0.93333	1.00000	1.00000	1.00000	0.85714	1.00000	1.00000	1.00000	1.00000	1.00000	0.71429	1.00000	1.00000	1.00000	1.00000	1
.00000	0.88889	1.00000	0.90909	1.00000	1.00000	1.00000	0.75000	1.00000	1.00000
0.91667	0.84211	0.71429	0.94118	0.80000	0.78571	0.94118	0.78571	0.80952	0.78571	0.83333	0.60000	0.66667	0.80000	0.66667	1.00000	0.63158	0.73810	1.00000	0.80952	0.77778	0.90909	0.87500	0.90909	1.00000	0
.95000	0.92000	0.77778	0.92308	0.83333	0.53846	0.68000	0.80000	0.57143	0.72727	0.61538	0.50000	0.66667	0.75000	0.70588	0.75000	1.00000	0.42857	0.75000	0.61538	0.71429	0.62500	0.58621	0.92308	0.92857	0
.52381	0.73077	0.53846	0.84615	0.76190	0.73333	0.62500	0.71429	0.81818	0.83333
1.00000	1.00000	0.80000	1.00000	    NaN	0.83333	0.66667	1.00000	1.00000	1.00000	0.81818	1.00000	1.00000	1.00000	1.00000	    NaN	0.86667	0.95238	0.50000	1.00000	0.80000	1.00000	1.00000	0.50000	1.00000	1
.00000	0.75000	1.00000	0.50000	1.00000	1.00000	0.92308	1.00000	1.00000	1.00000	1.00000	1.00000	1.00000	0.83333	0.78571	0.25000	1.00000	0.75000	1.00000	0.60000	0.63636	    NaN	0.75000	0.83333	0.94118	0
.60000	1.00000	1.00000	0.75000	0.84615	0.80000	1.00000	0.80000	0.75000	0.66667
'''
