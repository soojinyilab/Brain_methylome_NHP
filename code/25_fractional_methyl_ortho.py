import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'

flist = glob.glob("../summary_stat_all_ortho_cytosine/3_species_methyl_table/*_*_*_avgMeth.bed") #Human_ND_CG_avgMeth.bed

for sfile in flist:
    systemstr = "python summary_ortho_cytosine_methyl_level.py "+sfile
    run_systemstr = 'echo "cd '+wd+' && source activate stats && '
    run_systemstr = run_systemstr + systemstr
    run_systemstr = run_systemstr+'" | qsub -N '+sfile.split('/')[-1].split('.')[0]+' -q bioforce-6 -l nodes=1:ppn=1,walltime=10:00:00,mem=16gb'
    print (run_systemstr)
    os.system(run_systemstr)
            

#../1_merge_samples_CH_cytosine_report/0_merged_raw_cytosine_report/Human/Human_ND_chrchr1_CH.bed
