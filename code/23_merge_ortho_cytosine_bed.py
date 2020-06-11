import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'

#HCM_ND_chrchr15_CH.curated.bed  HCM_ND_chrchr21_CG.curated.bed  HCM_ND_chrchr6_CH.curated.bed   HCM_OD_chrchr13_CG.curated.bed  HCM_OD_chrchr19_CH.curated.bed  HCM_OD_chrchr4_CG.curated.bed   
#HCM_ND_chrchr16_CG.curated.bed  HCM_ND_chrchr21_CH.curated.bed  HCM_ND_chrchr7_CG.curated.bed   HCM_OD_chrchr13_CH.curated.bed  HCM_OD_chrchr1_CG.curated.bed   HCM_OD_chrchr4_CH.curated.bed   
#[hjeong84@login-s2 code]$ head ../4_informative_ortho_cytosine/curated/HCM_ND_chrchr10_CH.curated.bed 
#chr10	93615	93616	1/12,2/11,0/6,2/12,0/11,3/19,0/6,0/6,0/13,1/14..1/12,0/3,0/7,0/10,0/5,0/1,1/3,0/9,0/8,0/13..0/12,1/5,0/4,1/8,1/4,4/27,0/11,1/10,0/7,0/6
#chr10	93877	93878	0/9,1/11,0/6,1/15,1/7,0/8,1/7,0/13,1/19,1/9..0/8,0/1,0/15,0/12,0/14,0/0,0/13,0/11,0/10,0/14..0/3,0/3,0/1,0/2,0/5,0/14,1/8,0/1,0/7,0/9
            
in_file_dir = "../summary_stat_all_ortho_cytosine/1_avg_frac_methyl_table/tmp/"
out_file_dir = "../summary_stat_all_ortho_cytosine/1_avg_frac_methyl_table/"
stypes = ["CG","CH"]
for stype in stypes:
    sChrs = sorted([str(x) for x in range(1,23)])
    flist = [in_file_dir+"HCM_chrchr"+x+"_"+stype+"_avgMeth.txt" for x in sChrs] #../summary_stat_all_ortho_cytosine/1_avg_frac_methyl_table/tmp/HCM_chrchr22_CH_avgMeth.txt
    systemstr = "cat <(head -n +1 "+flist[0]+") <(tail -n +2 "+") <(tail -n +2 ".join(flist)+") > "+out_file_dir+"HCM_"+stype+"_avgMeth.txt" 
    run_systemstr = 'echo "cd '+wd+' && '
    run_systemstr = run_systemstr + systemstr
    run_systemstr = run_systemstr+'" | qsub -N '+stype+' -q bioforce-6 -l nodes=1:ppn=1,walltime=10:00:00,mem=32gb'
    print (run_systemstr)
    os.system(run_systemstr)



#../1_merge_samples_CH_cytosine_report/0_merged_raw_cytosine_report/Human/Human_ND_chrchr1_CH.bed
