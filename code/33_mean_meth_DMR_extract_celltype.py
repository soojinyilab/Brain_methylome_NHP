import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
#stypes = ["CH","CG"] #,"CH"]
#celltypes = ["ND","OD"]
#Chrs = ["chr"+str(x) for x in range(1,23)]
in_dir = "../6_DSS_output_ortho_cytosine/combined_celltype/" #../6_DSS_output_ortho_cytosine/combined_celltype/HCM_chrchr19_CH_Celltype.DMR.fdrs.filtered.txt
out_dir = "../7_results_celltype_DMR/1_avg_frac_methyl_table/tmp/"
rds_dir = "../5_DSS_input_ortho_cytosine/combined_celltype/rds/"

'''
[hjeong84@login-s4 code]$ mkdir ../7_results_species_DMR
[hjeong84@login-s4 code]$ mkdir ../7_results_species_DMR/1_avg_frac_methyl_table/tmp
[hjeong84@login-s4 code]$ mkdir ../7_results_species_DMR/2_DMR_output
[hjeong84@login-s4 code]$ mkdir ../7_results_species_DMR/3_filtered_DMR
[hjeong84@login-s4 code]$ mkdir ../7_results_species_DMR/4_filtered_DMR_bed

[hjeong84@login-s4 code]$ ls -l -h ../6_DSS_output_ortho_cytosine/split/HCM_*.DMR.fdrs.filtered.txt
-rw-r--r-- 1 hjeong84 bio-soojinyi  37K Jan 21 15:20 ../6_DSS_output_ortho_cytosine/split/HCM_ND_chrchr10_CG_Species_HvsC.DMR.fdrs.filtered.txt
-rw-r--r-- 1 hjeong84 bio-soojinyi  74K Jan 21 15:24 ../6_DSS_output_ortho_cytosine/split/HCM_ND_chrchr10_CG_Species_MvsC.DMR.fdrs.filtered.txt
-rw-r--r-- 1 hjeong84 bio-soojinyi  96K Jan 21 15:28 ../6_DSS_output_ortho_cytosine/split/HCM_ND_chrchr10_CG_Species_MvsH.DMR.fdrs.filtered.txt
-rw-r--r-- 1 hjeong84 bio-soojinyi  71K Jan 21 18:08 ../6_DSS_output_ortho_cytosine/split/HCM_ND_chrchr10_CH_Species_HvsC.DMR.fdrs.filtered.txt
-rw-r--r-- 1 hjeong84 bio-soojinyi 275K Jan 21 19:29 ../6_DSS_output_ortho_cytosine/split/HCM_ND_chrchr10_CH_Species_MvsC.DMR.fdrs.filtered.txt

[hjeong84@login-s4 code]$ more ../5_DSS_input_ortho_cytosine/split/rds/HCM_
HCM_ND_chrchr10_CG.rds  HCM_ND_chrchr15_CH.rds  HCM_ND_chrchr20_CG.rds  HCM_ND_chrchr4_CH.rds   HCM_OD_chrchr10_CG.rds  HCM_OD_chrchr15_CH.rds  HCM_OD_chrchr20_CG.rds  HCM_OD_chrchr4_CH.rds
HCM_ND_chrchr10_CH.rds  HCM_ND_chrchr16_CG.rds  HCM_ND_chrchr20_CH.rds  HCM_ND_chrchr5_CG.rds   HCM_OD_chrchr10_CH.rds  HCM_OD_chrchr16_CG.rds  HCM_OD_chrchr20_CH.rds  HCM_OD_chrchr5_CG.rds
HCM_ND_chrchr11_CG.rds  HCM_ND_chrchr16_CH.rds  HCM_ND_chrchr21_CG.rds  HCM_ND_chrchr5_CH.rds   HCM_OD_chrchr11_CG.rds  HCM_OD_chrchr16_CH.rds  HCM_OD_chrchr21_CG.rds  HCM_OD_chrchr5_CH.rds


HCM_chrchr15_CG_Celltype.DMR.fdrs.txt                 HCM_chrchr21_CH_Celltype_chimp.DMR.fdrs.txt           HCM_chrchr8_CG_Celltype.DMR.fdrs.txt
HCM_chrchr15_CH_Celltype_chimp.DMR.fdrs.filtered.txt  HCM_chrchr21_CH_Celltype.DMR.fdrs.filtered.txt        HCM_chrchr8_CH_Celltype_chimp.DMR.fdrs.filtered.txt
HCM_chrchr15_CH_Celltype_chimp.DMR.fdrs.txt           HCM_chrchr21_CH_Celltype.DMR.fdrs.txt                 HCM_chrchr8_CH_Celltype_chimp.DMR.fdrs.txt
HCM_chrchr15_CH_Celltype.DMR.fdrs.filtered.txt        HCM_chrchr21_CH_Celltype_human.DMR.fdrs.filtered.txt  HCM_chrchr8_CH_Celltype.DMR.fdrs.filtered.txt
'''
files = glob.glob(in_dir+"HCM_chrchr*_*_Celltype*.DMR.fdrs.filtered.txt")
for sfile in files:
    if os.path.exists(out_dir+sfile.split('/')[-1].split('.txt')[0]+".meth"):continue
    if "_CH" in sfile.split('/')[-1]:
        mem = "50"
    else:
        mem = "32"
    rds_file = rds_dir+sfile.split('/')[-1].split("_Celltype")[0]+".rds"
    systemstr = " && Rscript extract_grange_meth_mean_celltype.R "+rds_file+" "+sfile+" "+out_dir+sfile.split('/')[-1].split('.txt')[0]+".meth"
    run_systemstr = 'echo "cd '+wd+' && source activate CH '
    run_systemstr = run_systemstr + systemstr
    run_systemstr = run_systemstr+' && conda deactivate" | qsub -N '+sfile.split('/')[-1].split('.')[0]+' -q bioforce-6 -l nodes=1:ppn=1,walltime=3:00:00,mem='+mem+'gb'
    print (run_systemstr)
    os.system(run_systemstr)
    #sys.exit()
##############################################

