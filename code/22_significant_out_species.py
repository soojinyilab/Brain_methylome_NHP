import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
in_dir = "../7_results_species/2_fdr_DSS_output/"
out_dir = "../7_results_species/3_significant_sites/"
files = glob.glob(in_dir+"HCM_*_Species.fdr.txt")
for sfile in files:
    sfile_out = out_dir+sfile.split('/')[-1].replace(".fdr.txt",".fdr.sig.txt")
    ##strict output excludes H - C < fdr 0.05 for H and C vs M cases I prefer not using strict one
    #sfile_out2 = out_dir+sfile.split('/')[-1].replace(".fdr.txt",".fdr.sig.strict.txt")

    systemstr = " && python significant_sites_species.py "+sfile+" "+sfile_out
    run_systemstr = 'echo "cd '+wd+' && source activate CH'
    run_systemstr = run_systemstr + systemstr
    run_systemstr = run_systemstr+'" | qsub -N '+sfile.split('/')[-1]+' -q bioforce-6 -l nodes=1:ppn=1,walltime=10:00:00,mem=16gb'
    print (run_systemstr)
    os.system(run_systemstr)
##############################################

