import sys,glob,os

species = 'Chimp'
flist = glob.glob("/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/0_preprocessing/bedGraph_CG/"+species+"/*_CG_bedgraph.gz.bismark.cov.gz")
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/0_preprocessing/cytosine_report/CG/'+species+'/'
if species == "Chimp":
    genome_folder = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/reference/excluding_non_chromosomal/Chimp/'
if species == "Macaq":
    genome_folder = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/reference/excluding_non_chromosomal/Macaq/'

for sfile in flist:
    input_file = sfile
    sname = input_file.split('/')[-1].split('_CG_bedgraph.gz')[0]+'_CpG_report'
    systemstr = 'echo "cd '+wd+' && source activate DSS && '
    systemstr = systemstr + 'coverage2cytosine --genome_folder '+genome_folder+' --gzip --split_by_chromosome -o '+sname+' '+input_file 
    systemstr = systemstr+'" | qsub -N '+sname+' -q bioforce-6 -l nodes=1:ppn=1,walltime=10:00:00,mem=50gb'
    print (systemstr)
    os.system(systemstr)

'''
(DSS) [hjeong84@login-s4 code]$ more ../0_preprocessing/merged_CH_context/Chimp/CH_context_
CH_context_ABBY_ND.txt.gz     CH_context_BELEKA_ND.txt.gz   CH_context_CALLIE_ND.txt.gz   CH_context_LULU_ND.txt.gz     CH_context_MELISSA_ND.txt.gz  CH_context_Roger_ND.txt.gz

(DSS) [hjeong84@login-s4 code]$ ls ~/scratch/CH_methylation/
CHG_context_ABBY_ND_processed_bismark_bt2_pe.deduplicated.txt.gz     CHH_context_ABBY_OD_bismark_bt2_pe.deduplicated.txt.gz
'''
