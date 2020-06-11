import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
stypes = ["CH"]#,"CG"] #,"CH"]
celltypes = ["ND"]#,"OD"]
incomplete = ["10","12","1","2","3","4","5","7","9"]
for stype in stypes:
    for celltype in celltypes:
        human_in_dir = "../1_merge_samples_"+stype+"_cytosine_report/2_merged_excluding_lowDP_cytosine_report/Human/"
        human_files = glob.glob(human_in_dir+"Human_"+celltype+"_chrchr*_"+stype+".excSNP.DP.bed")
        liftover_in_dir = "../2_lifted_over_cytosine/"+stype+"/"
        ortho_out_dir = "../3_ortho_cytosine/"+stype+"/"
        sh_out_dir = "tmp_combine_species_liftover/"
        mem = "50"
        if stype == "CG":
            mem = "16"
        for sfile in human_files:
            sChr = sfile.split('/')[-1].split('_chrchr')[-1].split('_')[0]
            if sChr not in incomplete:continue
            human_input = sfile
            chimp_input = liftover_in_dir+"Chimp/hg19_Chimp_"+celltype+"_chrchr"+sChr+"_"+stype+".bed"
            macaq_input = liftover_in_dir+"Macaq/hg19_Macaq_"+celltype+"_chrchr"+sChr+"_"+stype+".bed"
            human_chimp_out = ortho_out_dir+"HC/HC_"+celltype+"_chrchr"+sChr+"_"+stype+".bed"
            human_chimp_macaq_out = ortho_out_dir+"HCM/HCM_"+celltype+"_chrchr"+sChr+"_"+stype+".bed"
            with open(sh_out_dir+celltype+"_"+sChr+"_"+stype+".sh",'w') as fout:
                systemstr_HC_intercept = "bedtools intersect -a "+human_input+" -b "+chimp_input+" -wa -wb | awk -v OFS='\\t' '"+'{print $1,$2,$3,$4".."$8}'+"' | sort -k1,1 -k2,2n > "+human_chimp_out
                systemstr_HCM_intercept = "bedtools intersect -a "+human_chimp_out+" -b "+macaq_input+" -wa -wb | awk -v OFS='\\t' '"+'{print $1,$2,$3,$4".."$8}'+"' | sort -k1,1 -k2,2n | uniq > "+human_chimp_macaq_out
                fout.write(systemstr_HC_intercept+'\n')
                fout.write(systemstr_HCM_intercept)
            run_systemstr = 'echo "cd '+wd+' && source activate stats'
            run_systemstr = run_systemstr + " && sh "+sh_out_dir+celltype+"_"+sChr+"_"+stype+".sh"
            run_systemstr = run_systemstr+'" | qsub -N '+sfile.split('/')[-1].split('.')[0]+' -q bioforce-6 -l nodes=1:ppn=1,walltime=20:00:00,mem='+mem+'gb'
            print (run_systemstr)
            os.system(run_systemstr)
'''
[hjeong84@login-s2 code]$ mkdir ../3_ortho_cytosine/CH/tmp
[hjeong84@login-s2 code]$ mkdir ../3_ortho_cytosine/CG/tmp
[hjeong84@login-s2 code]$ mkdir ../3_ortho_cytosine/CH/HC
[hjeong84@login-s2 code]$ mkdir ../3_ortho_cytosine/CH/HCM
[hjeong84@login-s2 code]$ mkdir ../3_ortho_cytosine/CG/HC
[hjeong84@login-s2 code]$ mkdir ../3_ortho_cytosine/CG/HCM
'''
#[hjeong84@login-s2 code]$ ls -l -h ../2_lifted_over_cytosine/CH/Chimp/hg19_Chimp_OD_chrchr11_CH.bed 
#../1_merge_samples_CH_cytosine_report/0_merged_raw_cytosine_report/Human/Human_ND_chrchr1_CH.bed

