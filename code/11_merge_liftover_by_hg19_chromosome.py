import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
stypes = ["CH","CG"] #,"CH"]
spes   = ["Chimp","Macaq"]
celltypes = ["ND","OD"]
valid_chr = ["chr"+str(x) for x in range(1,23)]
for spe in spes:
    for stype in stypes:
        for celltype in celltypes:
            split_chromosome_liftover_in_dir = "../2_lifted_over_cytosine/"+stype+"/tmp/tmp_chr/"
            flist = glob.glob(split_chromosome_liftover_in_dir+"split_hg19_*_"+spe+"_"+celltype+"_"+stype+".*")
            sChr_list = set([x.split('/')[-1].split('split_hg19_')[-1].split('_'+spe)[0] for x in flist])
            out_dir = "../2_lifted_over_cytosine/"+stype+"/"+spe+"/"
            for sChr in sChr_list:
                if sChr not in valid_chr:continue
                sChr_all_files = glob.glob(split_chromosome_liftover_in_dir+"split_hg19_"+sChr+"_"+spe+"_"+celltype+"_"+stype+".*")
                #sh_name = "../2_lifted_over_cytosine/"+stype+"/tmp/tmp_sh/"+"chromosome_merge_"+sChr+"_"+spe+"_"+celltype+"_"+stype+".sh"
                #fout = open(sh_name,'w')
                systemstr = 'cat '+' '.join(sChr_all_files)+' | sort -k1,1 -k2,2n > '+out_dir+"hg19_"+spe+"_"+celltype+"_chr"+sChr+"_"+stype+".bed"
                #fout.close()
                #systemstr = "bash "+sh_name
                run_systemstr = 'echo "cd '+wd+' && source activate stats && '
                run_systemstr = run_systemstr + systemstr
                run_systemstr = run_systemstr+'" | qsub -N '+"hg19_"+spe+"_"+celltype+"_chr"+sChr+"_"+stype+' -q bioforce-6 -l nodes=1:ppn=1,walltime=10:00:00,mem=8gb'
                print (run_systemstr)
                os.system(run_systemstr)

#../1_merge_samples_CH_cytosine_report/0_merged_raw_cytosine_report/Human/Human_ND_chrchr1_CH.bed

