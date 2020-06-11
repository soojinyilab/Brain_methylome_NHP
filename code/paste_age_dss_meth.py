import sys,os,glob

#flist = glob.glob("tmp_age_species_interaction/meth/HCM_*.meth")
flist = glob.glob("tmp_age_species_interaction_human_chimp/meth/*_DMR.meth")
for sfile in flist:
    DSS_DMR = sfile.split(".")[0].replace("/meth/","/merged/")+".grange"
    systemstr = "paste "+DSS_DMR+" "+sfile+" > ./tmp_age_species_interaction_human_chimp/paste/"+sfile.split('/')[-1].replace(".meth",".txt")
    print (systemstr)
    os.system(systemstr)
    




'''
(CH) [hjeong84@login-s3 code]$ more tmp_age_species_interaction/meth/HCM_OD_chrchr1_CG.meth 
AN03398_Control_Olig2,AN15240_Control_Olig2,AN16799_Control_Olig2,X1527_Control_Olig2,X1532_Control_Olig2,X1538_Control_Olig2,X1539_Control_Olig2,X1541_Control_Olig2,X3602_Control_Olig2,X46
15_Control_Olig2,ABBY_OD,ANJA_OD,BELEKA_OD,BJORN_OD,CALLIE_OD,DUNCAN_OD,LULU_OD,MELISSA_OD,OSSABAW_OD,Roger_OD,YN04-200_OD,YN08-380_OD,YN09-122_OD,YN09-173_OD,YN09-72_OD,YN11-300_OD,YN11-77
_OD,YN11-78_OD,YN12-654_OD,YN14-248_OD
0.2768,0.7149,0.6559,0.7439,0.3545,0.5825,0.5874,0.6576,0.2934,0.7191,0.3167,0.1500,0.1313,0.3839,0.4409,0.5107,0.2889,0.4324,0.2993,0.3762,0.5458,0.4656,0.5010,0.5532,0.5089,0.7083,0.5303,
0.5553,0.5296,0.6119

(CH) [hjeong84@login-s3 code]$ more tmp_age_species_interaction/
HCM_ND_chrchr10_CG_DML_Species_Age_interaction_fdrs.txt  HCM_ND_chrchr3_CG_DML_Species_Age_interaction_fdrs.txt   HCM_OD_chrchr18_CG_DML_Species_Age_interaction_fdrs.txt
HCM_ND_chrchr10_CG_DMR_Species_Age_interaction_fdrs.txt  HCM_ND_chrchr3_CG_DMR_Species_Age_interaction_fdrs.txt   HCM_OD_chrchr18_CG_DMR_Species_Age_interaction_fdrs.txt
HCM_ND_chrchr11_CG_DML_Species_Age_interaction_fdrs.txt  HCM_ND_chrchr4_CG_DML_Species_Age_interaction_fdrs.txt   HCM_OD_chrchr19_CG_DML_Species_Age_interaction_fdrs.txt
HCM_ND_chrchr11_CG_DMR_Species_Age_interaction_fdrs.txt  HCM_ND_chrchr4_CG_DMR_Species_Age_interaction_fdrs.txt   HCM_OD_chrchr19_CG_DMR_Species_Age_interaction_fdrs.txt
HCM_ND_chrchr12_CG_DML_Species_Age_interaction_fdrs.txt  HCM_ND_chrchr5_CG_DML_Species_Age_interaction_fdrs.txt   HCM_OD_chrchr1_CG_DML_Species_Age_interaction_fdrs.tx

'''

