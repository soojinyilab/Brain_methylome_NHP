import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
stypes = ["CG"]#["CG","CH"]
spes   = ["Human","Chimp","Macaq"]
snp_dir = "../../WGS/snp_bed/" #Human/C_SNP_Human_1.bed"

for spe in spes:
    for stype in stypes:
        in_file_dir = "../1_merge_samples_"+stype+"_cytosine_report/0_merged_raw_cytosine_report/"+spe+"/"
        out1_file_dir = "../1_merge_samples_"+stype+"_cytosine_report/1_merged_excluding_SNP_cytosine_report/"+spe+"/"
        out2_file_dir = "../1_merge_samples_"+stype+"_cytosine_report/2_merged_excluding_lowDP_cytosine_report/"+spe+"/"

        flist = glob.glob(in_file_dir+spe+"_*_chrchr*_"+stype+".bed")
        for sfile in flist:
            sname1 = sfile.split('/')[-1].replace(".bed",".excSNP.bed")
            sname2 = sname1.replace(".excSNP.bed",".excSNP.DP.bed")
            iChr = sfile.split('/')[-1].split("chrchr")[-1].split('_')[0]
            snp_file = snp_dir+spe+'/C_SNP_'+spe+"_chr"+iChr+".bed"
            systemstr1 = "bedtools subtract -a "+sfile+" -b "+snp_file+" > "+out1_file_dir+sname1
            systemstr2 = "python lowDP.py "+out1_file_dir+sname1+" "+out2_file_dir+sname2
            #print (systemstr)
            
            run_systemstr = 'echo "cd '+wd+' && source activate stats && '
            run_systemstr = run_systemstr + systemstr1+' && '
            run_systemstr = run_systemstr + systemstr2
            run_systemstr = run_systemstr+'" | qsub -N '+sname1+' -q bioforce-6 -l nodes=1:ppn=1,walltime=1:00:00,mem=16gb'
            print (run_systemstr)
            os.system(run_systemstr)
            

#../1_merge_samples_CH_cytosine_report/0_merged_raw_cytosine_report/Human/Human_ND_chrchr1_CH.bed
