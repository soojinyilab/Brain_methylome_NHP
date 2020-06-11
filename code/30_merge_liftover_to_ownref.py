import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
stypes = ["CG","CH"]#,"CG"] #,"CH"]
spes   = ["panTro5","rheMac8"]
nCPU = 8
for spe in spes:
    for stype in stypes:
        split_liftover_in_dir = "../summary_stat_all_ortho_cytosine/4_liftover_species_methyl_table/tmp/tmp_"+spe+"/"
        flist = glob.glob(split_liftover_in_dir+"split_"+spe+"_"+stype+"_avgMeth.x*")
        #../summary_stat_all_ortho_cytosine/4_liftover_species_methyl_table/tmp/tmp_panTro5/split_panTro5_CG_avgMeth.xaa
        out_dir = "../summary_stat_all_ortho_cytosine/4_liftover_species_methyl_table/tmp/tmp_"+spe+"_chr/"
        sh_name = "../summary_stat_all_ortho_cytosine/4_liftover_species_methyl_table/tmp/tmp_sh/"+"chromosome_distribute_"+spe+"_"+stype+".sh"
        fout = open(sh_name,'w')
        for sfile in flist:
            fout.write('python2 split_by_chrom_ownref.py '+sfile+' '+spe+'\n')
        fout.close()

        systemstr = "python2 multi_exec_per_line.py "+sh_name+' '+str(nCPU)
        run_systemstr = 'echo "cd '+wd+' && source activate stats && '
        run_systemstr = run_systemstr + systemstr
        run_systemstr = run_systemstr+'" | qsub -N '+sh_name.split('/')[-1]+' -q bioforce-6 -l nodes=1:ppn=8,walltime=10:00:00,mem=32gb'
        print (run_systemstr)
        os.system(run_systemstr)

#../1_merge_samples_CH_cytosine_report/0_merged_raw_cytosine_report/Human/Human_ND_chrchr1_CH.bed

