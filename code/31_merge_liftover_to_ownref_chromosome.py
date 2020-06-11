import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
stypes = ["CH","CG"] #,"CH"]
spes   = ["panTro5","rheMac8"]
valid_chr_panTro5 = ["chr"+str(x) for x in range(1,23)]+["chr2A","chr2B"]
valid_chr_rheMac8 = ["chr"+str(x) for x in range(1,21)]
for spe in spes:
    for stype in stypes:
            split_chromosome_liftover_in_dir = "../summary_stat_all_ortho_cytosine/4_liftover_species_methyl_table/tmp/tmp_"+spe+"_chr/"
            flist = glob.glob(split_chromosome_liftover_in_dir+"split_"+spe+"_chr*_"+stype+"_avgMeth.x*")
            sChr_list = set([x.split('/')[-1].split('split_'+spe+'_')[-1].split('_'+stype)[0] for x in flist])
            if spe == "panTro5":
                valid_chr = valid_chr_panTro5
            elif spe == "rheMac8":
                valid_chr = valid_chr_rheMac8
            else:
                print ("error")
                sys.exit()
            for sChr in sChr_list:
                if sChr not in valid_chr:continue
                sChr_all_files = glob.glob(split_chromosome_liftover_in_dir+"split_"+spe+"_"+sChr+"_"+stype+"_avgMeth.x*")
                systemstr = 'cat '+' '.join(sChr_all_files)+' | sort -k1,1 -k2,2n > '+split_chromosome_liftover_in_dir+spe+"_"+sChr+"_"+stype+".bed"
                run_systemstr = 'echo "cd '+wd+' && source activate stats && '
                run_systemstr = run_systemstr + systemstr
                run_systemstr = run_systemstr+'" | qsub -N '+spe+"_"+sChr+"_"+stype+' -q bioforce-6 -l nodes=1:ppn=1,walltime=10:00:00,mem=8gb'
                print (run_systemstr)
                os.system(run_systemstr)

'''
z    1499991 ../summary_stat_all_ortho_cytosine/4_liftover_species_methyl_table/tmp/tmp_panTro5_chr/split_panTro5_chr12_CH_avgMeth.xcy
^C
[hjeong84@login-s4 code]$ ls -l -h ../summary_stat_all_ortho_cytosine/4_liftover_species_methyl_table/tmp/tmp_panTro5_chr/split_panTro5_chr* | wc -l
'''
