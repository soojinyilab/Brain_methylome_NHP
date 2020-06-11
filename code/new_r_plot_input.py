import sys,os,glob
dd_cov = {}
with open('../../bsseq/matrix/covariates_all.txt','r') as fCovariates:
    for line in fCovariates:
        line_temp = line.strip().split('\t')
        dd_cov[line_temp[0]] = line_temp[5]

celltypes = ["NeuN","OLIG2"]
Types = ["_Age_","_interSpeAge_"]
for Type in Types:
    for celltype in celltypes:
        cnt = 0
        dd_H = set()
        dd_C = set()
        dd_M = set()
        dd_idx = {}
        with open("tmp_age_species_interaction_human_chimp/paste/hg19_"+celltype+Type+"DMR.txt",'r') as fH:
            fH.seek(0)
            fH.readline()
            for line in fH:
                line_temp = line.strip().split('\t')
                dd_H.add(line_temp[3])
                dd_idx[line_temp[3]] = ('_'.join(line_temp[0:3]),str(int(line_temp[2]) - int(line_temp[1])))
        with open("tmp_age_species_interaction_human_chimp/paste/panTro5_"+celltype+Type+"DMR.txt",'r') as fH:
            fH.seek(0)
            fH.readline()
            for line in fH:
                line_temp = line.strip().split('\t')
                dd_C.add(line_temp[3])
        with open("tmp_age_species_interaction_human_chimp/paste/rheMac8_"+celltype+Type+"DMR.txt",'r') as fH:
            fH.seek(0)
            fH.readline()
            for line in fH:
                line_temp = line.strip().split('\t')
                dd_M.add(line_temp[3])

            
        dd_overlap = set()
    
        for i in dd_H:
            if i in dd_C and i in dd_M:
                dd_overlap.add(i)

        fout = open("tmp_age_species_interaction_human_chimp/plot_input/"+celltype+Type+"sig_DMR.txt",'w')
        fout.write("index\tLocus\tLength\tMethylation\tSample\tAge_group\tSpecies\n")

        with open("tmp_age_species_interaction_human_chimp/paste/hg19_"+celltype+Type+"DMR.txt",'r') as fp:
            fp.seek(0)
            samples = fp.readline().strip().split('\t')[-1].split(',')
            ages = [dd_cov[x] for x in samples]
            spes = ["Human"]*len(samples)
            if celltype == "NeuN":
                cell_idx = "NeuN"
            if celltype == "OLIG2":
                cell_idx = "Olig2"
            for line in fp:
                line_temp = line.strip().split('\t')
                if line_temp[3] not in dd_overlap:continue
                locus = dd_idx[line_temp[3]][0]
                Length = dd_idx[line_temp[3]][1]
                meths = line_temp[-1].split(',')
                for i in range(len(meths)):
                    if cell_idx not in samples[i]:continue
                    if "Control" not in samples[i]:continue
                    fout.write(line_temp[3]+'\t'+locus+'\t'+Length+'\t'+meths[i]+'\t'+samples[i]+'\t'+ages[i]+'\t'+spes[i]+'\n')

        with open("tmp_age_species_interaction_human_chimp/paste/panTro5_"+celltype+Type+"DMR.txt",'r') as fp:
            fp.seek(0)
            samples = fp.readline().strip().split('\t')[-1].split(',')
            ages = [dd_cov[x] for x in samples]
            spes = ["Chimpanzee"]*len(samples) 
            if celltype == "NeuN":
                cell_idx = "ND"
            if celltype == "OLIG2":
                cell_idx = "OD"
            for line in fp:
                line_temp = line.strip().split('\t')
                if line_temp[3] not in dd_overlap:continue
                locus = dd_idx[line_temp[3]][0]
                Length = dd_idx[line_temp[3]][1]
                meths = line_temp[-1].split(',')
                for i in range(len(meths)):
                    if cell_idx not in samples[i]:continue
                    fout.write(line_temp[3]+'\t'+locus+'\t'+Length+'\t'+meths[i]+'\t'+samples[i]+'\t'+ages[i]+'\t'+spes[i]+'\n')

        with open("tmp_age_species_interaction_human_chimp/paste/rheMac8_"+celltype+Type+"DMR.txt",'r') as fp:
            fp.seek(0)
            samples = fp.readline().strip().split('\t')[-1].split(',')
            ages = [dd_cov[x] for x in samples]
            spes = ["Macaque"]*len(samples)
            if celltype == "NeuN":
                cell_idx = "ND"
            if celltype == "OLIG2":
                cell_idx = "OD"
            for line in fp:
                line_temp = line.strip().split('\t')
                if line_temp[3] not in dd_overlap:continue
                locus = dd_idx[line_temp[3]][0]
                Length = dd_idx[line_temp[3]][1]
                meths = line_temp[-1].split(',')
                for i in range(len(meths)):
                    if cell_idx not in samples[i]:continue
                    fout.write(line_temp[3]+'\t'+locus+'\t'+Length+'\t'+meths[i]+'\t'+samples[i]+'\t'+ages[i]+'\t'+spes[i]+'\n')
        fout.close()
        
'''
[hjeong84@login-s3 code]$ cd tmp_age_species_interaction_human_chimp/paste/
hg19_NeuN_Age_DMR.txt              hg19_OLIG2_interSpeAge_DMR.txt     panTro5_OLIG2_Age_DMR.txt          rheMac8_NeuN_interSpeAge_DMR.txt   
hg19_NeuN_interSpeAge_DMR.txt      panTro5_NeuN_Age_DMR.txt           panTro5_OLIG2_interSpeAge_DMR.txt  rheMac8_OLIG2_Age_DMR.txt         

chr	start	end	index	AN03398_Control_NeuN,AN16799_Control_NeuN,Miami0001_Control_NeuN,X3545_Control_NeuN,AN15240_Control_NeuN,X1541_Control_NeuN,X3586_Control_NeuN,X1532_Control_NeuN,X3611_Control_NeuN,AN10090_Control_NeuN,X1531_Control_NeuN,X3590_Control_NeuN,X4615_Control_NeuN,X1538_Control_NeuN,X1524_Control_NeuN,X1534_Control_NeuN,X1525_Control_NeuN,X1539_Control_NeuN,X3602_Control_NeuN,X1527_Control_NeuN,X1536_Control_NeuN,AN05483_Control_NeuN,X1533_Control_NeuN,X1535_Control_NeuN,X1537_Control_NeuN,X3590_Control_Olig2,X3611_Control_Olig2,X1525_Control_Olig2,Miami0001_Control_Olig2,X3545_Control_Olig2,X1536_Control_Olig2,X3586_Control_Olig2,AN15240_Control_Olig2,AN16799_Control_Olig2,X3602_Control_Olig2,AN03398_Control_Olig2,X1541_Control_Olig2,X1538_Control_Olig2,X1539_Control_Olig2,AN10090_Control_Olig2,X1527_Control_Olig2,X1524_Control_Olig2,AN05483_Control_Olig2,X4615_Control_Olig2,X1532_Control_Olig2
chr6	10720972	10721086	idx1	0.65591,0.91366,0.90163,0.76592,0.91041,0.60460,0.68927,0.78230,0.65176,0.58471,0.82616,0.62968,0.75777,0.61921,0.68210,0.61895,0.49310,0.78297,0.62732,0.89837,0.56387,0.36457,0.89630,0.80556,0.70198,0.72778,0.55988,0.52202,0.77054,0.49116,0.45263,0.45683,0.79686,0.63584,0.62052,0.56168,0.70728,0.36577,0.75177,0.67496,0.77991,0.41799,0.70929,0.75496,0.77185
chr6	28829640	28829764	idx2	0.95163,0.82397,0.71258,0.86893,0.68952,0.82787,0.77699,0.80831,0.74492,0.74733,0.74878,0.76328,0.79515,0.78693,0.82484,0.88166,0.90914,0.67080,0.91948,0.72365,0.69277,0.83213,0.82591,0.79379,0.76939,0.96565,0.93614,0.93195,0.93958,0.96696,0.91027,0.94493,0.94898,0.97552,0.93491,0.89958,0.92169,0.95283,0.84434,0.93433,0.93514,0.93326,0.91819,0.93351,0.92740

'''


'''
(CH) [hjeong84@login-s3 code]$ head ../../bsseq/matrix/covariates_all.txt
GT_ID	UTSW_ID	Species	CellType	Sex	Age_Class	Pmi	Conversion_rates	mean_depth
ABBY_ND	Abby_Chimp_NeuN	Chimp	NeuN	F	2	0.9	0.997066985	27.39180763
ABBY_OD	Abby_Chimp_Olig2	Chimp	Olig	F	2	0.9	0.997474197	19.66345141
ANJA_ND	Anja_Chimp_NeuN	Chimp	NeuN	F	3	0.9	0.996175952	13.67905407
ANJA_OD	Anja_Chimp_Olig2	Chimp	Olig	F	3	0.9	0.988650199	10.28
BELEKA_ND	Beleka	Chimp	NeuN	F	3	0.5	0.998109846	22.99399376
BELEKA_OD	Beleka_Chimp_Olig2	Chimp	Olig	F	3	0.5	0.997243503	17.28481718
BJORN_ND	Bjorn_Chimp_NeuN	Chimp	NeuN	M	1	3	0.998330605	3.377732443
BJORN_OD	Bjorn_Chimp_Olig2	Chimp	Olig	M	1	3	0.998275521	9.097123051



(CH) [hjeong84@login-s3 code]$ more tmp_age_species_interaction/paste/HCM_OD_chrchr11_CG.meth 
chr	start	end	length	nCG	areaStat	AN03398_Control_Olig2,AN15240_Control_Olig2,AN16799_Control_Olig2,X1527_Control_Olig2,X1532_Control_Olig2,X1538_Control_Olig2,X1539_C
ontrol_Olig2,X1541_Control_Olig2,X3602_Control_Olig2,X4615_Control_Olig2,ABBY_OD,ANJA_OD,BELEKA_OD,BJORN_OD,CALLIE_OD,DUNCAN_OD,LULU_OD,MELISSA_OD,OSSABAW_OD,Roger_OD,YN04-200_OD,YN08-380_O
D,YN09-122_OD,YN09-173_OD,YN09-72_OD,YN11-300_OD,YN11-77_OD,YN11-78_OD,YN12-654_OD,YN14-248_OD
chr11	130781542	130781664	123	6	17.471176229698	0.501,0.915,0.651,0.939,0.476,0.818,0.870,0.895,0.602,0.237,0.447,0.222,0.417,0.800,0.581,0.239,0.533,0.463,0.694,0.2
49,0.601,0.401,0.516,0.598,0.688,0.663,0.622,0.674,0.618,0.641
'''
