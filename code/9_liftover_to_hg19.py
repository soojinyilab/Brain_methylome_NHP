import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
stypes = ["CH","CG"] #,"CH"]
spes   = ["Chimp","Macaq"]

for spe in spes:
    for stype in stypes:
        tmp_split_in_dir = "../2_lifted_over_cytosine/"+stype+"/tmp/"
        flist = glob.glob(tmp_split_in_dir+"split_"+spe+"_*_"+stype+".*")
        out_name = "../2_lifted_over_cytosine/"+stype+"/tmp/tmp_sh/"+"merged_liftover_input_"+spe+"_"+stype+".sh"
        '''
        fout = open(out_name,'w')
        lifted_out_dir = tmp_split_in_dir+"tmp_hg19/"
        if spe == "Chimp":
            lifted_chain = "/nv/hp10/hjeong84/data/references/human/liftOver/panTro5ToHg19.over.chain"
        elif spe == "Macaq":
            lifted_chain = "/nv/hp10/hjeong84/data/references/human/liftOver/rheMac8ToHg19.over.chain"
        for sfile in flist:
            fout.write("liftOver "+sfile+" "+lifted_chain+" "+lifted_out_dir+sfile.replace(spe+"_","hg19_"+spe+"_").split("/")[-1]+" "+lifted_out_dir+"unmapped/"+sfile.replace(spe+"_","unmapped_"+spe+"_").split('/')[-1]+'\n')
        fout.close()
        '''
        out_name_split = out_name.replace("/merged_","/split_")+'.'
        systemstr_split = "split -l 4 "+out_name+" "+out_name_split
        print (systemstr_split)
        #os.system(systemstr_split)
        #os.system("rm "+out_name)

        flist_sh = glob.glob(out_name_split+"*")
        for sfile_sh in flist_sh:
            
            systemstr = "python2 multi_liftover_sh.py "+sfile_sh
            #print (systemstr)
            run_systemstr = 'echo "cd '+wd+' && source activate liftover && '
            run_systemstr = run_systemstr + systemstr
            run_systemstr = run_systemstr+'" | qsub -N '+sfile_sh.split('/')[-1]+' -q bioforce-6 -l nodes=1:ppn=4,walltime=32:00:00,mem=32gb'
            print (run_systemstr)
            os.system(run_systemstr)

#../1_merge_samples_CH_cytosine_report/0_merged_raw_cytosine_report/Human/Human_ND_chrchr1_CH.bed
