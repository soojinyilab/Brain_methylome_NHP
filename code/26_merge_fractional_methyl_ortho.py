import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'

flist = glob.glob("../summary_stat_all_ortho_cytosine/3_species_methyl_table/*_*_*_avgMeth.summary.proportion") #Human_ND_CG_avgMeth.bed

with open("../summary_stat_all_ortho_cytosine/3_species_methyl_table/Summary_proportion_mC_ortho.merge",'w') as fout:
    fout.write("ctype\tspecies\tcelltype\tM_level\tvalue\n")
    for sfile in flist:
        with open(sfile,'r') as fp:
            for line in fp:
                fout.write(line)
            
flist = glob.glob("../summary_stat_all_ortho_cytosine/3_species_methyl_table/*_*_*_avgMeth.summary.count")

with open("../summary_stat_all_ortho_cytosine/3_species_methyl_table/Summary_count_mC_ortho.merge",'w') as fout:
    fout.write("ctype\tspecies\tcelltype\tM_level\tvalue\n")
    for sfile in flist:
        with open(sfile,'r') as fp:
            for line in fp:
                fout.write(line)


#../1_merge_samples_CH_cytosine_report/0_merged_raw_cytosine_report/Human/Human_ND_chrchr1_CH.bed
