import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
spes   = ["Chimp","Macaq"]

for spe in spes:
    tmp_split_in_dir = "../2_lifted_over_cytosine/identify_duplicated_mapping/tmp/"
    flist = glob.glob(tmp_split_in_dir+"split_"+spe+".*")
    out_name = "../2_lifted_over_cytosine/identify_duplicated_mapping/tmp/tmp_sh/"+"merged_liftover_input_"+spe+".sh"
    
    fout = open(out_name,'w')
    lifted_out_dir = tmp_split_in_dir+"tmp_hg19/"
    if spe == "Chimp":
        lifted_chain = "/nv/hp10/hjeong84/data/references/human/liftOver/panTro5ToHg19.over.chain"
    elif spe == "Macaq":
        lifted_chain = "/nv/hp10/hjeong84/data/references/human/liftOver/rheMac8ToHg19.over.chain"
    for sfile in flist:
        fout.write("liftOver "+sfile+" "+lifted_chain+" "+lifted_out_dir+sfile.replace(spe,"hg19_"+spe).split("/")[-1]+" "+lifted_out_dir+"unmapped/"+sfile.replace(spe,"unmapped_"+spe).split('/')[-1]+'\n')
    fout.close()
    
    out_name_split = out_name.replace("/merged_","/split_")+'.'
    
    systemstr_split = "split -l 3 "+out_name+" "+out_name_split
    print (systemstr_split)
    os.system(systemstr_split)
    #os.system("rm "+out_name)
    
    flist_sh = glob.glob(out_name_split+"*")
    for sfile_sh in flist_sh:
        #if not (sfile_sh.split('/')[-1] == "split_liftover_input_Chimp.sh.eb" or sfile_sh.split('/')[-1] == "split_liftover_input_Macaq.sh.da"):continue
        systemstr = "python2 multi_liftover_sh.py "+sfile_sh
        #print (systemstr)
        run_systemstr = 'echo "cd '+wd+' && source activate liftover && '
        run_systemstr = run_systemstr + systemstr
        run_systemstr = run_systemstr+'" | qsub -N '+sfile_sh.split('/')[-1]+' -q bioforce-6 -l nodes=1:ppn=4,walltime=15:00:00,mem=50gb'
        print (run_systemstr)
        os.system(run_systemstr)

#../1_merge_samples_CH_cytosine_report/0_merged_raw_cytosine_report/Human/Human_ND_chrchr1_CH.bed
