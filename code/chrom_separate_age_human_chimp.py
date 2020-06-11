import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
#stypes = ["CH","CG"] #,"CH"]
#celltypes = ["ND","OD"]
#Chrs = ["chr"+str(x) for x in range(1,23)]
out_dir = "./tmp_age_species_interaction_human_chimp/"
#in_dir = "../5_DSS_input_ortho_cytosine/split/rds/"
#files = glob.glob(in_dir+"HCM_*_chrchr*_CG.rds")
files = ["../../bsseq/human_chimp_hg19_NeuN.Rds","../../bsseq/human_chimp_hg19_OLIG2.Rds"]
#remain = ["HCM_OD_chrchr4_CH","HCM_ND_chrchr19_CG","HCM_ND_chrchr17_CH","HCM_ND_chrchr20_CG","HCM_ND_chrchr13_CH","HCM_OD_chrchr15_CH","HCM_ND_chrchr20_CH"]
for sfile in files:
    if "NeuN" in sfile:
        human_idx = "Control"
        chimp_idx = "_ND"
    elif "OLIG2" in sfile:
        human_idx = "Control"
        chimp_idx = "_OD"
    for i in range(1,23):
        if not ("NeuN" in sfile and i == 4):continue
        sChr = "chr"+str(i)
        args_idx1,args_idx2,args_idx3,args_idx4,args_idx5 = sfile,human_idx,chimp_idx,sChr,out_dir+"rds/"+sChr+"_human_chimp_"+sfile.split('/')[-1].split('_')[-1]
        systemstr = " && Rscript bs_split.R "+args_idx1+" "+args_idx2+" "+args_idx3+" "+args_idx4+" "+args_idx5
        run_systemstr = 'echo "cd '+wd+' && source activate CH '
        run_systemstr = run_systemstr + systemstr
        run_systemstr = run_systemstr+' && conda deactivate" | qsub -N age_'+sfile.split('/')[-1].split('.')[0]+' -q bioforce-6 -l nodes=1:ppn=2,walltime=2:00:00,mem=32gb'
        print (run_systemstr)
        os.system(run_systemstr)
    
##############################################
#(CH) [hjeong84@login-s3 code]$ cp run_DSS_age_human_chimp.R run_DSS_species_age_interaction_human_chimp.R 

