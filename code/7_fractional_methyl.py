import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
stypes = ["CG","CH"]
spes   = ["Human","Chimp","Macaq"]

for spe in spes:
    for stype in stypes:
        in_file_dir = "../1_merge_samples_"+stype+"_cytosine_report/2_merged_excluding_lowDP_cytosine_report/"+spe+"/"
        flist = glob.glob(in_file_dir+spe+"_*_chrchr*_"+stype+".excSNP.DP.bed")
        for sfile in flist:
            systemstr = "python fill_lowDP_calculate_avg.py "+sfile
            run_systemstr = 'echo "cd '+wd+' && source activate stats && '
            run_systemstr = run_systemstr + systemstr
            run_systemstr = run_systemstr+'" | qsub -N '+sfile.split('/')[-1].split('.')[0]+' -q bioforce-6 -l nodes=1:ppn=1,walltime=4:00:00,mem=16gb'
            print (run_systemstr)
            os.system(run_systemstr)
            

#../1_merge_samples_CH_cytosine_report/0_merged_raw_cytosine_report/Human/Human_ND_chrchr1_CH.bed
