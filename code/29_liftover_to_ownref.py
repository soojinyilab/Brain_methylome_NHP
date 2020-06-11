import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
spes   = ["Chimp","Macaq"]
tmp_in_dir = "../summary_stat_all_ortho_cytosine/4_liftover_species_methyl_table/tmp/"
flist = glob.glob(tmp_in_dir+"split_*.x*")
flag = 0
complete_list_pantro = set([x.split("_panTro5_")[-1] for x in glob.glob(tmp_in_dir+"tmp_panTro5/split_panTro5_*.x*")])
complete_list_rheMac = set([x.split("_rheMac8_")[-1] for x in glob.glob(tmp_in_dir+"tmp_rheMac8/split_rheMac8_*.x*")])
complete_list = complete_list_pantro.intersection(complete_list_rheMac)  #set(complete_list_pantro+complete_list_rheMac)
#print (complete_list)
print (len(complete_list))
#sys.exit()
for sfile in flist:
    if sfile.split('/')[-1].split('_hg19_')[-1] in complete_list:continue# == "split_hg19_CH_avgMeth.xks":
    lifted_out_chimp = tmp_in_dir+"tmp_panTro5/"
    lifted_out_macaq = tmp_in_dir+"tmp_rheMac8/"
    lifted_chain_chimp = "/nv/hp10/hjeong84/data/references/human/liftOver/hg19ToPanTro5.over.chain"
    lifted_chain_macaq = "/nv/hp10/hjeong84/data/references/human/liftOver/hg19ToRheMac8.over.chain"
    systemstr_chimp = "liftOver "+sfile+" "+lifted_chain_chimp+" "+lifted_out_chimp+sfile.split('/')[-1].replace("_hg19_","_panTro5_")+" "+lifted_out_chimp+"unmapped/"+sfile.split('/')[-1].replace('split_',"unmapped_split_")
    systemstr_macaq = "liftOver "+sfile+" "+lifted_chain_macaq+" "+lifted_out_macaq+sfile.split('/')[-1].replace("_hg19_","_rheMac8_")+" "+lifted_out_macaq+"unmapped/"+sfile.split('/')[-1].replace('split_',"unmapped_split_")
    
    run_systemstr = 'echo "cd '+wd+' && source activate liftover && '
    run_systemstr = run_systemstr + systemstr_chimp+" && "+systemstr_macaq
    run_systemstr = run_systemstr+'" | qsub -N '+sfile.split('/')[-1]+' -q bioforce-6 -l nodes=1:ppn=1,walltime=24:00:00,mem=12gb'
    print (run_systemstr)
    #os.system(run_systemstr)
    #sys.exit()

#../1_merge_samples_CH_cytosine_report/0_merged_raw_cytosine_report/Human/Human_ND_chrchr1_CH.bed
