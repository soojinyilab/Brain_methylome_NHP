import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
stypes = ["CG","CH"]#["CG","CH"]

for stype in stypes:
    in_file_dir = "../summary_stat_all_ortho_cytosine/4_liftover_species_methyl_table/"#hg19_CG_avgMeth.bed
    tmp_merge_dir = "../summary_stat_all_ortho_cytosine/4_liftover_species_methyl_table/tmp/"
    if stype == "CG":
        lNum = 1000000
    if stype == "CH":
        lNum = 1500000
    lNum = str(lNum)
    systemstr_split = "split -l "+lNum+" "+in_file_dir+"hg19_"+stype+'_avgMeth.bed '+tmp_merge_dir+"split_hg19_"+stype+'_avgMeth.x'
    print (systemstr_split)
    os.system(systemstr_split)



'''
        for sfile in flist:
            sname1 = sfile.split('/')[-1].replace(".bed",".excSNP.bed")
            sname2 = sname1.replace(".excSNP.bed",".excSNP.DP.bed")
            iChr = sfile.split('/')[-1].split("chrchr")[-1].split('_')[0]
            snp_file = snp_dir+spe+'/C_SNP_'+spe+"_"+iChr+".bed"
            systemstr1 = "bedtools subtract -a "+sfile+" -b "+snp_file+" > "+out1_file_dir+sname1
            systemstr2 = "python lowDP.py "+out1_file_dir+sname1+" "+out2_file_dir+sname2
            #print (systemstr)
            
            run_systemstr = 'echo "cd '+wd+' && source activate stats && '
            run_systemstr = run_systemstr + systemstr1+' && '
            run_systemstr = run_systemstr + systemstr2
            run_systemstr = run_systemstr+'" | qsub -N '+sname1+' -q bioforce-6 -l nodes=1:ppn=1,walltime=1:00:00,mem=16gb'
            print (run_systemstr)
            os.system(run_systemstr)
'''         

#../1_merge_samples_CH_cytosine_report/0_merged_raw_cytosine_report/Human/Human_ND_chrchr1_CH.bed
