import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
#stypes = ["CH","CG"] #,"CH"]
#celltypes = ["ND","OD"]
#Chrs = ["chr"+str(x) for x in range(1,23)]
out_dir = "../6_DSS_output_ortho_cytosine/split/"
in_dir = "../5_DSS_input_ortho_cytosine/split/rds/"
files = glob.glob(in_dir+"HCM_*_chrchr*_*.rds")
#remain = ["HCM_OD_chrchr4_CH","HCM_ND_chrchr19_CG","HCM_ND_chrchr17_CH","HCM_ND_chrchr20_CG","HCM_ND_chrchr13_CH","HCM_OD_chrchr15_CH","HCM_ND_chrchr20_CH"]
for sfile in files:
    #if not ("chrchr2_" in sfile.split('/')[-1].split('.')[0] and "_CH" in sfile and "_ND" in sfile):continue
    if "_CG" in sfile:
        mem_size = "16"
    elif "_CH" in sfile:
        mem_size = "32"
    if "_CH" in sfile and ("chrchr1_" in sfile or "chrchr2_" in sfile or "chrchr3_" in sfile or "chrchr4_" in sfile or "chrchr5_" in sfile):
        mem_size = "50"
    systemstr = " && Rscript run_DSS_species.R "+sfile+" "+out_dir+sfile.split('/')[-1].split('.')[0]
    run_systemstr = 'echo "cd '+wd+' && source activate CH '
    run_systemstr = run_systemstr + systemstr
    run_systemstr = run_systemstr+' && conda deactivate" | qsub -N '+sfile.split('/')[-1].split('.')[0]+' -q bioforce-6 -l nodes=1:ppn=1,walltime=20:00:00,mem='+mem_size+'gb'
    print (run_systemstr)
    os.system(run_systemstr)
    #sys.exit()
##############################################

