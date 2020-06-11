import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
in_dir = "../7_results_species/2_fdr_DSS_output/tmp/"
files = glob.glob(in_dir+"HCM_*_Species*.txt")
for sfile in files:
    if not ("_ND" in sfile and "_CH" in sfile and "_Species_HvsC.txt" in sfile):continue
    sfile_out = sfile.replace(".txt",".fdr.txt")
    systemstr = " && Rscript add_fdr.R "+sfile+" "+sfile_out
    run_systemstr = 'echo "cd '+wd+' && source activate CH'
    run_systemstr = run_systemstr + systemstr
    run_systemstr = run_systemstr+'" | qsub -N '+sfile.split('/')[-1]+' -q bioforce-6 -l nodes=1:ppn=1,walltime=20:00:00,mem=64gb'
    print (run_systemstr)
    os.system(run_systemstr)
##############################################

