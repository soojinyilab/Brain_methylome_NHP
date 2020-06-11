import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
in_dir = "../5_DSS_input_ortho_cytosine/*/table/"
files = glob.glob(in_dir+"HCM*_chrchr*_*_Info.txt")

#rds_list = glob.glob("../5_DSS_input_ortho_cytosine/split/rds/*.rds")

for sfile in files:
    mem = "16"
    if "_CH" in sfile:
        mem = "50"
    info_table = str(sfile)
    cov_table = sfile.replace("_Info.txt","_Cov.txt")
    M_table = sfile.replace("_Info.txt","_M.txt")
    out_file_name = sfile.replace("/table/","/rds/").replace('_Info.txt','.rds')
    #if out_file_name in rds_list:continue
    systemstr = " && Rscript make_table2rds.R "+info_table+" "+cov_table+' '+M_table+' '+out_file_name
    run_systemstr = 'echo "cd '+wd+' && source activate CH'
    run_systemstr = run_systemstr + systemstr
    run_systemstr = run_systemstr+' && conda deactivate" | qsub -N '+sfile.split('/')[-1].split('.')[0]+' -q bioforce-6 -l nodes=1:ppn=1,walltime=10:00:00,mem='+mem+'gb'
    print (run_systemstr)
    os.system(run_systemstr)
##############################################
sys.exit()
#############################################
'''
in_dir = "../5_DSS_input_ortho_cytosine/all_merged/table/"
files = glob.glob(in_dir+"HCM_*_*_Info.txt")
out_dir = "../5_DSS_input_ortho_cytosine/combined/rds/"

for sfile in files:
    mem = "32"
    if "CH" in sfile and "ND" in sfile:
        mem = "128"
        continue
    info_table = str(sfile)
    cov_table = sfile.replace("_Info.txt","_Cov.txt")
    M_table = sfile.replace("_Info.txt","_M.txt")
    out_file_name = out_dir+sfile.split('/')[-1].split('_Info.txt')[0]+".rds"
    systemstr = " && Rscript make_table2rds.R "+info_table+" "+cov_table+' '+M_table+' '+out_file_name
    run_systemstr = 'echo "cd '+wd+' && source activate CH '
    run_systemstr = run_systemstr + systemstr
    run_systemstr = run_systemstr+' && conda deactivate" | qsub -N '+sfile.split('/')[-1].split('.')[0]+' -q bioforce-6 -l nodes=1:ppn=1,walltime=5:00:00,mem='+mem+'gb'
    print (run_systemstr)
    os.system(run_systemstr)
'''


'''
[hjeong84@login-s4 code]$ head ../3_ortho_cytosine/CH/HCM/HCM_ND_chrchr22_CH.bed 
chr22	17111641	17111642	0/10,0/15,0/15,0/9,0/17,0/12,0/13,0/16,0/17,0/12..1/22,0/7,0/11,0/20,0/23,0/7,0/8,0/18,0/14,0/22..0/7,0/6,0/9,0/7,0/7,0/13,0/2,0/9,0/4,0/4
chr22	17111655	17111656	0/9,0/13,0/11,0/8,0/14,0/10,0/15,0/16,0/16,0/15..1/22,0/8,2/13,0/22,2/21,0/8,1/8,0/17,0/14,0/21..0/10,0/6,0/9,0/8,0/7,0/13,0/3,0/11,0/4,0/5
chr22	17111662	17111663	0/20,0/20,1/23,1/10,0/26,1/18,0/19,0/16,0/17,0/14..0/19,0/15,0/17,0/23,0/16,0/3,0/20,0/21,0/10,1/25..0/13,0/12,0/12,1/2,0/10,0/20,1/17,0/17,1/11,0/9
chr22	17111673	17111674	0/12,0/12,0/12,1/7,0/14,0/9,0/13,0/17,0/12,0/12..2/22,1/8,3/12,0/20,2/20,0/9,1/9,0/20,0/14,1/21..2/10,1/8,2/11,3/8,0/6,1/13,1/4,3/11,2/4,2/5
chr22	17111681	17111682	1/11,1/10,0/11,1/7,2/16,1/8,3/13,0/16,1/11,0/13..1/21,1/8,3/12,1/21,2/21,0/9,0/11,3/20,1/14,2/20..2/10,0/8,0/11,1/8,2/6,4/13,1/4,0/11,1/4,0/4

[hjeong84@login-s2 code]$ mkdir ../3_ortho_cytosine/CH/tmp
[hjeong84@login-s2 code]$ mkdir ../3_ortho_cytosine/CG/tmp
[hjeong84@login-s2 code]$ mkdir ../3_ortho_cytosine/CH/HC
[hjeong84@login-s2 code]$ mkdir ../3_ortho_cytosine/CH/HCM
[hjeong84@login-s2 code]$ mkdir ../3_ortho_cytosine/CG/HC
[hjeong84@login-s2 code]$ mkdir ../3_ortho_cytosine/CG/HCM
'''
#[hjeong84@login-s2 code]$ ls -l -h ../2_lifted_over_cytosine/CH/Chimp/hg19_Chimp_OD_chrchr11_CH.bed 
#../1_merge_samples_CH_cytosine_report/0_merged_raw_cytosine_report/Human/Human_ND_chrchr1_CH.bed

