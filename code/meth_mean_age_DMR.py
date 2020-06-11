import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
#stypes = ["CH","CG"] #,"CH"]
#celltypes = ["ND","OD"]
#Chrs = ["chr"+str(x) for x in range(1,23)]
in_dir = "./tmp_age_species_interaction/"
out_dir = "./tmp_age_species_interaction/meth/"
rds_dir = "../5_DSS_input_ortho_cytosine/split/rds/"

'''
(CH) [hjeong84@login-s3 code]$ head tmp_age_species_interaction/
HCM_ND_chrchr10_CG_DML_Species_Age_interaction_fdrs.txt  HCM_ND_chrchr3_CG_DML_Species_Age_interaction_fdrs.txt   HCM_OD_chrchr18_CG_DML_Species_Age_interaction_fdrs.txt
HCM_ND_chrchr10_CG_DMR_Species_Age_interaction_fdrs.txt  HCM_ND_chrchr3_CG_DMR_Species_Age_interaction_fdrs.txt   HCM_OD_chrchr18_CG_DMR_Species_Age_interaction_fdrs.txt
HCM_ND_chrchr11_CG_DML_Species_Age_interaction_fdrs.txt  HCM_ND_chrchr4_CG_DML_Species_Age_interaction_fdrs.txt   HCM_OD_chrchr19_CG_DML_Species_Age_interaction_fdrs.txt
'''
files = glob.glob(rds_dir+"HCM_*_chrchr*_CG.rds")
#remain = ["HCM_OD_chrchr4_CH","HCM_ND_chrchr19_CG","HCM_ND_chrchr17_CH","HCM_ND_chrchr20_CG","HCM_ND_chrchr13_CH","HCM_OD_chrchr15_CH","HCM_ND_chrchr20_CH"]
for sfile in files:
    #if not ("chrchr2_" in sfile.split('/')[-1].split('.')[0] and "_CH" in sfile and "_ND" in sfile):continue
    systemstr = " && Rscript extract_grange_meth.R "+sfile+" "+in_dir+sfile.split('/')[-1].split('.')[0]+"_DMR_Species_Age_interaction_fdrs.txt"+" "+out_dir+sfile.split('/')[-1].split('.')[0]+".meth"
    run_systemstr = 'echo "cd '+wd+' && source activate CH '
    run_systemstr = run_systemstr + systemstr
    run_systemstr = run_systemstr+' && conda deactivate" | qsub -N '+sfile.split('/')[-1].split('.')[0]+' -q bioforce-6 -l nodes=1:ppn=1,walltime=1:00:00,mem=32gb'
    print (run_systemstr)
    os.system(run_systemstr)
    #sys.exit()
##############################################

