import sys,os,glob

flist = glob.glob("Chimp*.bed")
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CG_meth_ownref/ownref2/chimp_tmp/'
for sfile in flist:
    systemstr = 'echo "cd '+wd+' && source activate liftover && '
    systemstr = systemstr + "liftOver "+sfile+" ~/data/references/human/liftOver/panTro5ToHg19.over.chain "+sfile.replace("Chimp_","hg19_Chimp_")+" "+sfile.replace("Chimp_","unmapped_Chimp_")
    systemstr = systemstr+'" | qsub -N liftover -q bioforce-6 -l nodes=1:ppn=1,walltime=3:00:00,mem=12gb'
    print (systemstr)
    os.system(systemstr)

