import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
#stypes = ["CH","CG"] #,"CH"]
#celltypes = ["ND","OD"]
#Chrs = ["chr"+str(x) for x in range(1,23)]
in_dir = "../7_results_species_DMR/1_avg_frac_methyl_table/tmp/"
files = glob.glob(in_dir+"HCM_*_chrchr1_*_Species_*.meth")
#out_dir = "../7_results_species_DMR/2_fdr_DSS_output/tmp/"
avg_methyl_in_dir = "../7_results_species_DMR/1_avg_frac_methyl_table/"
DMR_out_dir = "../7_results_species_DMR/2_DMR_output/tmp/"
'''
in_dir = "../6_DSS_output_ortho_cytosine/split/"
out_dir = "../7_results_species_DMR/1_avg_frac_methyl_table/tmp/"
rds_dir = "../5_DSS_input_ortho_cytosine/split/rds/"

[hjeong84@login-s4 code]$ mkdir ../7_results_species_DMR
[hjeong84@login-s4 code]$ mkdir ../7_results_species_DMR/1_avg_frac_methyl_table/tmp
[hjeong84@login-s4 code]$ mkdir ../7_results_species_DMR/2_DMR_output
[hjeong84@login-s4 code]$ mkdir ../7_results_species_DMR/3_filtered_DMR
[hjeong84@login-s4 code]$ mkdir ../7_results_species_DMR/4_filtered_DMR_bed

-rw-r--r-- 1 hjeong84 bio-soojinyi  74K Jan 21 15:24 ../6_DSS_output_ortho_cytosine/split/HCM_ND_chrchr10_CG_Species_MvsC.DMR.fdrs.filtered.txt
-rw-r--r-- 1 hjeong84 bio-soojinyi  96K Jan 21 15:28 ../6_DSS_output_ortho_cytosine/split/HCM_ND_chrchr10_CG_Species_MvsH.DMR.fdrs.filtered.txt
-rw-r--r-- 1 hjeong84 bio-soojinyi  71K Jan 21 18:08 ../6_DSS_output_ortho_cytosine/split/HCM_ND_chrchr10_CH_Species_HvsC.DMR.fdrs.filtered.txt
-rw-r--r-- 1 hjeong84 bio-soojinyi 275K Jan 21 19:29 ../6_DSS_output_ortho_cytosine/split/HCM_ND_chrchr10_CH_Species_MvsC.DMR.fdrs.filtered.txt

'''

for sfile in files:
    sfile_index_front = sfile.split('_chrchr')[0]+"_chrchr"
    sfile_index_end   = '_'+'_'.join(sfile.split('_chrchr')[-1].split('_')[1:])
    flist_chrs = [sfile_index_front+str(x)+sfile_index_end for x in range(1,23)]
    #flist_chrs = glob.glob(sfile.split('_chrchr')[0]+"*_"+sfile.split('_')[-2]+"_Species.txt")
    flist_chrs = ["<(tail -n +2 "+x+")" for x in flist_chrs]
   
    sfile_index_front2 = "../6_DSS_output_ortho_cytosine/split/"+sfile.split('_chrchr')[0].split('/')[-1]+"_chrchr"
    sfile_index_end2   = sfile_index_end.replace(".meth",".txt")
    flist_chrs2 = [sfile_index_front2+str(x)+sfile_index_end2 for x in range(1,23)]
    flist_chrs2 = ["<(tail -n +2 "+x+")" for x in flist_chrs2]
    
    systemstr = " && cat header_species.txt "+' '.join(flist_chrs)+" > "+avg_methyl_in_dir+sfile.split('/')[-1].split('_chrchr')[0]+sfile_index_end
    systemstr2 = " && cat header_DMR.txt "+' '.join(flist_chrs2)+" > "+DMR_out_dir+sfile.split('/')[-1].split('_chrchr')[0]+sfile_index_end2
    run_systemstr = 'echo "cd '+wd+' '
    run_systemstr = run_systemstr + systemstr+systemstr2
    run_systemstr = run_systemstr+'" | qsub -N '+sfile.split('/')[-1].split('.')[0]+' -q bioforce-6 -l nodes=1:ppn=1,walltime=10:00:00,mem=32gb'
    print (run_systemstr)
    os.system(run_systemstr)
    #sys.exit()

'''
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
'''



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

