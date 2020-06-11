import sys,glob,os

dd_CH = {}
spe = "Macaq"
flist = glob.glob("/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/0_preprocessing/merged_CH_context/"+spe+"/CH_context_YN04-200_OD*.txt.gz")
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/0_preprocessing/merged_CH_context/'+spe+'/'
new_loc = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/0_preprocessing/chromosomal_merged_CH_context/'+spe+'/'
for sfile in flist:
    input_file = sfile.split('/')[-1]
    sname = input_file.split('CH_context_')[-1].split('.txt')[0]
    fout = open('tmp/remove_non_chrom_'+sname+'.sh','w')
    fout.write("zcat "+wd+input_file+" | awk '{if ($3 !~ /_/) print $0}' | gzip -c > "+new_loc+input_file)
    fout.close()
    systemstr = 'echo "cd '+wd+' && source activate DSS && '
    systemstr = systemstr + 'sh /nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code/tmp/remove_non_chrom_'+sname+'.sh'
    systemstr = systemstr+'" | qsub -N '+sname+' -q bioforce-6 -l nodes=1:ppn=1,walltime=70:00:00,mem=16gb'
    print (systemstr)
    os.system(systemstr)


#cat test.txt | awk '{if ($3 !~ /_/) print $0}' | gzip -c > test.txt.gz

'''
(DSS) [hjeong84@login-s4 code]$ more ../0_preprocessing/merged_CH_context/Chimp/CH_context_
CH_context_ABBY_ND.txt.gz     CH_context_BELEKA_ND.txt.gz   CH_context_CALLIE_ND.txt.gz   CH_context_LULU_ND.txt.gz     CH_context_MELISSA_ND.txt.gz  CH_context_Roger_ND.txt.gz
CH_context_ABBY_OD.txt.gz     CH_context_BELEKA_OD.txt.gz   CH_context_CALLIE_OD.txt.gz   CH_context_LULU_OD.txt.gz     CH_context_MELISSA_OD.txt.gz  CH_context_Roger_OD.txt.gz
CH_context_ANJA_ND.txt.gz     CH_context_BJORN_ND.txt.gz    CH_context_DUNCAN_ND.txt.gz   CH_context_LYK_ND.txt.gz      CH_context_OSSABAW_ND.txt.gz  
CH_context_ANJA_OD.txt.gz     CH_context_BJORN_OD.txt.gz    CH_context_DUNCAN_OD.txt.gz   CH_context_LYK_OD.txt.gz      CH_context_OSSABAW_OD.txt.gz  



(DSS) [hjeong84@login-s4 code]$ ls ~/scratch/CH_methylation/
CHG_context_ABBY_ND_processed_bismark_bt2_pe.deduplicated.txt.gz     CHH_context_ABBY_OD_bismark_bt2_pe.deduplicated.txt.gz
CHG_context_ABBY_OD_bismark_bt2_pe.deduplicated.txt.gz               CHH_context_ANJA_ND_processed_bismark_bt2_pe.deduplicated.txt.gz
CHG_context_ANJA_ND_processed_bismark_bt2_pe.deduplicated.txt.gz     CHH_context_ANJA_OD_bismark_bt2_pe.deduplicated.txt.gz
CHG_context_ANJA_OD_bismark_bt2_pe.deduplicated.txt.gz               CHH_context_BELEKA_ND_bismark_bt2_pe.deduplicated.txt.gz
CHG_context_BELEKA_ND_bismark_bt2_pe.deduplicated.txt.gz             CHH_context_BELEKA_OD_bismark_bt2_pe.deduplicated.txt.gz

#PBS -N 3_1505ODM_concat_dedup_CH_report
#PBS -q bioforce-6
#PBS -l nodes=1:ppn=1
#PBS -l walltime=72:00:00
#PBS -l mem=50gb
#PBS -o 3_1505ODM_concat_dedup_CH_report.run
#PBS -j oe
#PBS -M ixa.mendizabal@gmail.com
#PBS -m a
cd $PBS_O_WORKDIR
module load samtools
cat CHH_context_1505ODM_concat.deduplicated.txt.gz CHG_context_1505ODM_concat.deduplicated.txt.gz > CH_context_1505ODM_concat.deduplicated.txt.gz
/nv/hp10/imendizabal3/data2/applications/bismark_v0.14.5/bismark2bedGraph --CX --buffer_size 50% --ample_memory -o 1505ODM_concat.deduplicated_CH_bedgraph CH_context_1505ODM_concat.deduplicated.txt.gz
/nv/hp10/imendizabal3/data2/applications/bismark_v0.14.5/coverage2cytosine --CX --split_by_chromosome --genome_folder /nv/hp10/imendizabal3/data2/applications/GRCh37/ -o 1505ODM_concat.deduplicated_CH_report 1505ODM_concat.deduplicated_CH_bedgraph.gz.bismark.cov.gz
'''
