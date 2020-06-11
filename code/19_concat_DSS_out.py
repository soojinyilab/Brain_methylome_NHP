import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
#stypes = ["CH","CG"] #,"CH"]
#celltypes = ["ND","OD"]
#Chrs = ["chr"+str(x) for x in range(1,23)]
in_dir = "../6_DSS_output_ortho_cytosine/split/"
files = glob.glob(in_dir+"HCM_*_chrchr1_*_Species*.txt")
out_dir = "../7_results_species/2_fdr_DSS_output/tmp/"
avg_methyl_in_dir = "../7_results_species/1_avg_frac_methyl_table/"

'''
HCM_ND_chrchr14_CH_Species.txt       HCM_ND_chrchr5_CG_Species_HvsC.txt   HCM_OD_chrchr15_CG_Species_MvsC.txt  HCM_OD_chrchr3_CH_Species_MvsH.txt
HCM_ND_chrchr15_CG_Species_HvsC.txt  HCM_ND_chrchr5_CG_Species_MvsC.txt   HCM_OD_chrchr15_CG_Species_MvsH.txt  HCM_OD_chrchr3_CH_Species.txt
[hjeong84@login-s4 code]$ head ../6_DSS_output_ortho_cytosine/split/HCM_OD_chrchr3_CH_Species.txt 
chr	pos	stat	pvals	fdrs
chr3	100254	2.50335974459791	0.0123020429075095	0.0665796710434941
chr3	100317	0.918687325000704	0.358259141397368	0.448731154332238

[hjeong84@login-s4 code]$ more ../7_results/1_avg_frac_methyl_table/HCM_
HCM_ND_chrchr10_CG_avgMeth.txt  HCM_ND_chrchr19_CG_avgMeth.txt  HCM_ND_chrchr6_CG_avgMeth.txt   HCM_OD_chrchr15_CG_avgMeth.txt  HCM_OD_chrchr2_CG_avgMeth.txt
HCM_ND_chrchr10_CH_avgMeth.txt  HCM_ND_chrchr19_CH_avgMeth.txt  HCM_ND_chrchr6_CH_avgMeth.txt   HCM_OD_chrchr15_CH_avgMeth.txt  HCM_OD_chrchr2_CH_avgMeth.txt
'''

for sfile in files:
    sfile_index_front = sfile.split('_chrchr')[0]+"_chrchr"
    sfile_index_end   = '_'+'_'.join(sfile.split('_chrchr')[-1].split('_')[1:])
    flist_chrs = [sfile_index_front+str(x)+sfile_index_end for x in range(1,23)]
    #flist_chrs = glob.glob(sfile.split('_chrchr')[0]+"*_"+sfile.split('_')[-2]+"_Species.txt")
    flist_chrs = ["<(tail -n +2 "+x+" | cut -f 1,2,3,4)" for x in flist_chrs]
    
    systemstr = " && cat tmp_header_universal.txt "+' '.join(flist_chrs)+" > "+out_dir+sfile.split('/')[-1].split('_chrchr')[0]+sfile_index_end
    run_systemstr = 'echo "cd '+wd+' '
    run_systemstr = run_systemstr + systemstr
    run_systemstr = run_systemstr+'" | qsub -N '+sfile.split('/')[-1].split('.')[0]+' -q bioforce-6 -l nodes=1:ppn=1,walltime=10:00:00,mem=32gb'
    print (run_systemstr)
    os.system(run_systemstr)
    #sys.exit()

files = glob.glob(avg_methyl_in_dir+"HCM_*_chrchr1_*_avgMeth.txt")

for sfile in files:
    sfile_index_front = sfile.split('_chrchr')[0]+"_chrchr"
    sfile_index_end   = '_'+'_'.join(sfile.split('_chrchr')[-1].split('_')[1:])
    flist_chrs = [sfile_index_front+str(x)+sfile_index_end for x in range(1,23)]
    #flist_chrs = glob.glob(sfile.split('_chrchr')[0]+"*_"+sfile.split('_')[-2]+"_Species.txt")
    flist_chrs = ["<(tail -n +2 "+x+")" for x in flist_chrs]

    systemstr = " && cat tmp_header_avg_meth_species.txt "+' '.join(flist_chrs)+" > "+out_dir+sfile.split('/')[-1].split('_chrchr')[0]+sfile_index_end
    run_systemstr = 'echo "cd '+wd+' '
    run_systemstr = run_systemstr + systemstr
    run_systemstr = run_systemstr+'" | qsub -N '+sfile.split('/')[-1].split('.')[0]+' -q bioforce-6 -l nodes=1:ppn=1,walltime=10:00:00,mem=16gb'
    print (run_systemstr)
    os.system(run_systemstr)
    #sys.exit()




##############################################


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

