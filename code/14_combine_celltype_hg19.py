import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
stypes = ["CH","CG"] #,"CH"]
for stype in stypes:
    in_dir = "../4_informative_ortho_cytosine/curated/"
    ND_files = glob.glob(in_dir+"HCM_ND_chrchr*_"+stype+".curated.bed")
    loci_tmp_out_dir = "../4_informative_ortho_cytosine/curated_merged/tmp/"
    out_dir = "../4_informative_ortho_cytosine/curated_merged/"
    sh_out_dir = "tmp_combine_bed/"
    mem = "32"
    if stype == "CG":
        mem = "16"
    for sfile in ND_files:
        sChr = sfile.split('/')[-1].split('_chrchr')[-1].split('_')[0]
        if not (sChr == "17"):continue
        ND_file = sfile
        OD_file = sfile.replace("_ND_","_OD_")
        out_file_index = sfile.replace("_ND_","_").split('/')[-1].split('.')[0]
        with open(sh_out_dir+sChr+"_"+stype+".sh",'w') as fout:
            systemstr = "bedtools intersect -a <(cut -f 1,2,3 "+ND_file+" | sort -k1,1 -k2,2n) -b <(cut -f 1,2,3 "+OD_file+" | sort -k1,1 -k2,2n) > "+loci_tmp_out_dir+out_file_index+".loci"
            systemstr = systemstr + '\n'
            systemstr = systemstr + "bedtools intersect -a "+ND_file+" -b "+loci_tmp_out_dir+out_file_index+".loci -wa | sort -k1,1 -k2,2n | uniq > "+loci_tmp_out_dir+out_file_index+".ND"
            systemstr = systemstr + '\n'
            systemstr = systemstr + "bedtools intersect -a "+OD_file+" -b "+loci_tmp_out_dir+out_file_index+".loci -wa | sort -k1,1 -k2,2n | uniq > "+loci_tmp_out_dir+out_file_index+".OD"
            systemstr = systemstr + '\n'
            systemstr = systemstr + "paste "+loci_tmp_out_dir+out_file_index+".ND "+loci_tmp_out_dir+out_file_index+".OD | awk -v OFS='\\t' '"+'{print $1,$2,$3,$4".."$8}'+"' > "+out_dir+out_file_index+".curated.bed"
            fout.write(systemstr)
        run_systemstr = 'echo "cd '+wd+' && source activate stats'
        run_systemstr = run_systemstr + " && bash "+sh_out_dir+sChr+"_"+stype+".sh"
        run_systemstr = run_systemstr+'" | qsub -N '+sfile.split('/')[-1].split('.')[0]+' -q bioforce-6 -l nodes=1:ppn=1,walltime=20:00:00,mem='+mem+'gb'
        print (run_systemstr)
        os.system(run_systemstr)



'''
[hjeong84@login-s2 code]$ mkdir ../3_ortho_cytosine/CH/tmp
[hjeong84@login-s2 code]$ mkdir ../3_ortho_cytosine/CG/tmp
[hjeong84@login-s2 code]$ mkdir ../3_ortho_cytosine/CH/HC
[hjeong84@login-s2 code]$ mkdir ../3_ortho_cytosine/CH/HCM
[hjeong84@login-s2 code]$ mkdir ../3_ortho_cytosine/CG/HC
[hjeong84@login-s2 code]$ mkdir ../3_ortho_cytosine/CG/HCM
'''
#[hjeong84@login-s2 code]$ ls -l -h ../2_lifted_over_cytosine/CH/Chimp/hg19_Chimp_OD_chrchr11_CH.bed 
#../1_merge_samples_CH_cytosine_report/0_merged_raw_cytosine_report/Human/Human_ND_chrchr1_CH.bed

