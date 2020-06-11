import sys,glob,os

dd_CH = {}

#flist_chimp = glob.glob("/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/0_preprocessing/CH_context/Chimp/CHH_*.txt.gz")
flist_macaq = glob.glob("/nv/hp10/hjeong84/scratch/CH_methylation/Macaq/CHH_*YN04-200_OD*.txt.gz")
#dd_CH["Chimp"] = flist_chimp
dd_CH["Macaq"] = flist_macaq

wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/0_preprocessing/'

for spe in dd_CH:
    for sfile in dd_CH[spe]:
        if spe == "Human":
            continue
        else:
            sname = sfile.split('/')[-1].split('_bismark_')[0].split('_processed')[0].split('context_')[-1]
        CHH = str(sfile)
        CHG = str(sfile).replace('CHH_','CHG_')
        
        systemstr = 'echo "cd '+wd+' && source activate DSS && '
        systemstr = systemstr+'cat '+CHH+' '+CHG+' > merged_CH_context/'+spe+'/CH_context_'+sname+'.txt.gz'
        #systemstr = systemstr + 'bismark2bedGraph --CX --buffer_size 50% --ample_memory -o ./bedGraph/'+spe+'/'+sname+'_CH_bedgraph '+'<(cat '+CHH+' '+CHG+')'
        systemstr = systemstr+'" | qsub -N '+sname+' -q bioforce-6 -l nodes=1:ppn=1,walltime=15:00:00,mem=20gb'
        print (systemstr)
        os.system(systemstr)




'''
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
