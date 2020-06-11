import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
stypes = ["CH"]#["CG","CH"]
spes   = ["Chimp","Macaq"]

for spe in spes:
    for stype in stypes:
        in_file_dir = "../1_merge_samples_"+stype+"_cytosine_report/2_merged_excluding_lowDP_cytosine_report/"+spe+"/"
        tmp_merge_dir = "../2_lifted_over_cytosine/"+stype+"/tmp/"
        flist_ND = glob.glob(in_file_dir+spe+"_ND_chrchr*_"+stype+".excSNP.DP.bed")
        flist_OD = glob.glob(in_file_dir+spe+"_OD_chrchr*_"+stype+".excSNP.DP.bed")
        systemstr_merge_ND = "cat "+' '.join(flist_ND)+" > "+tmp_merge_dir+"merge_"+spe+"_ND_"+stype+'.bed'
        systemstr_merge_OD = "cat "+' '.join(flist_OD)+" > "+tmp_merge_dir+"merge_"+spe+"_OD_"+stype+'.bed'
        print (systemstr_merge_ND,len(flist_ND))
        os.system(systemstr_merge_ND)
        print (systemstr_merge_OD,len(flist_OD))
        os.system(systemstr_merge_OD)
        if stype == "CG":
            lNum = 2000000
        if stype == "CH":
            lNum = 6000000
        lNum = str(lNum)
        systemstr_split_ND = "split -l "+lNum+" "+tmp_merge_dir+"merge_"+spe+"_ND_"+stype+'.bed '+tmp_merge_dir+"split_"+spe+"_ND_"+stype+'.'
        systemstr_split_OD = "split -l "+lNum+" "+tmp_merge_dir+"merge_"+spe+"_OD_"+stype+'.bed '+tmp_merge_dir+"split_"+spe+"_OD_"+stype+'.'
        print (systemstr_split_ND)
        os.system(systemstr_split_ND)
        print (systemstr_split_OD)
        os.system(systemstr_split_OD)
        os.system('rm '+tmp_merge_dir+"merge_"+spe+"_ND_"+stype+'.bed')
        os.system('rm '+tmp_merge_dir+"merge_"+spe+"_OD_"+stype+'.bed')



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
