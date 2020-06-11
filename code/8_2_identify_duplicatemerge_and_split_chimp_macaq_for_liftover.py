import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
#../0_preprocessing/cytosine_report_cut/CH/Chimp/Chimp_CH.chrchr
spe = "Human"
in_file_dir = "../0_preprocessing/cytosine_report_cut/CH/"+spe+"/"
tmp_merge_dir = "../2_lifted_over_cytosine/identify_duplicated_mapping_many2one/tmp/"
flist = glob.glob(in_file_dir+spe+"_CH.chrchr*.bed")
print (flist)
#sys.exit()
with open("identify_duplicate_cat_idx_all_cytosine_"+spe+".sh",'w') as fout:
    fout.write("cat "+' '.join(flist)+" | awk -v OFS='\\t' 'BEGIN{idx=0}{idx+=1; print $0,"+'idx'+"}' > "+tmp_merge_dir+"merge_"+spe+".bed")
lNum = 3000000
lNum = str(lNum)
systemstr_split = "split -l "+lNum+" "+tmp_merge_dir+"merge_"+spe+".bed "+tmp_merge_dir+"split_"+spe+'.x'
run_systemstr = 'echo "cd '+wd
run_systemstr = run_systemstr + ' && sh identify_duplicate_cat_idx_all_cytosine_'+spe+'.sh'
run_systemstr = run_systemstr + ' && '+systemstr_split
run_systemstr = run_systemstr+'" | qsub -N identify_duplicate_idx -q bioforce-6 -l nodes=1:ppn=1,walltime=15:00:00,mem=64gb'
print (run_systemstr)
os.system(run_systemstr)
