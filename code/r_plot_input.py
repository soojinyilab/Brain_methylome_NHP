import sys,os,glob
dd_cov = {}
with open('../../bsseq/matrix/covariates_all.txt','r') as fCovariates:
    for line in fCovariates:
        line_temp = line.strip().split('\t')
        dd_cov[line_temp[0]] = line_temp[5]

celltypes = ["ND","OD"]
for celltype in celltypes:
    cnt = 0
    flist = glob.glob("tmp_age_species_interaction/paste/HCM_"+celltype+"_chrchr*_CG.meth")
    fout = open("tmp_age_species_interaction/plot_input/"+celltype+"_age_sig_DMR.txt",'w')
    fout.write("index\tLocus\tnCG\tSignificance\tMethylation\tSample\tAge_group\tSpecies\n")
    for sfile in flist:
        with open(sfile,'r') as fp:
            samples = fp.readline().strip().split('\t')[-1].split(',')
            ages = [dd_cov[x] for x in samples]
            spes = ["Human"]*10 + ["Chimpanzee"]*10 + ["Macaque"]*10
            for line in fp:
                cnt +=1
                line_temp = line.strip().split('\t')
                locus = '_'.join(line_temp[0:3])
                nCG = line_temp[4]
                sig = line_temp[5]
                meths = line_temp[-1].split(',')
                for i in range(len(meths)):
                    fout.write(str(cnt)+'\t'+locus+'\t'+nCG+'\t'+sig+'\t'+meths[i]+'\t'+samples[i]+'\t'+ages[i]+'\t'+spes[i]+'\n')
fout.close()
        


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
