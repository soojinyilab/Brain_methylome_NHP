import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
spes   = ["Human"]
nCPU = 8
for spe in spes:
    split_liftover_in_dir = "../2_lifted_over_cytosine/identify_duplicated_mapping_many2one/tmp/tmp_panTro5/"
    flist = glob.glob(split_liftover_in_dir+"split_panTro5_"+spe+".*")
    out_dir = "../2_lifted_over_cytosine/identify_duplicated_mapping_many2one/tmp/tmp_chr/"
    sh_name = "../2_lifted_over_cytosine/identify_duplicated_mapping_many2one/tmp/tmp_sh/"+"chromosome_distribute_"+spe+".sh"
    fout = open(sh_name,'w')
    for sfile in flist:
        fout.write('python2 identify_duplicate_split_by_chrom_panTro5.py '+sfile+'\n')
    fout.close()
    systemstr = "python2 multi_exec_per_line.py "+sh_name+' '+str(nCPU)
    run_systemstr = 'echo "cd '+wd+' && source activate stats && '
    run_systemstr = run_systemstr + systemstr
    run_systemstr = run_systemstr+'" | qsub -N '+sh_name.split('/')[-1]+' -q bioforce-6 -l nodes=1:ppn=8,walltime=18:00:00,mem=32gb'
    print (run_systemstr)
    os.system(run_systemstr)

#../1_merge_samples_CH_cytosine_report/0_merged_raw_cytosine_report/Human/Human_ND_chrchr1_CH.bed

