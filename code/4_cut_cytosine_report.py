import sys,os,glob
wd = '/nv/hp10/hjeong84/data/Projects/WGBS_NHP/CH_methylation/code'
flist = glob.glob("../0_preprocessing/cytosine_report/C*/*/*_C*_report.chrchr1.C*_report.txt.gz")
stypes = ["CG"]#["CG","CH"]
spes   = ["Human","Chimp","Macaq"]
out_sh_dir = "tmp_cut/"
out_file_dir = "../0_preprocessing/cytosine_report_cut/"
for spe in spes:
    for stype in stypes:
        flist = glob.glob("../0_preprocessing/cytosine_report/"+stype+"/"+spe+"/*_report.chrchr1.*_report.txt.gz")
        for sfile in flist:
            loc = '/'.join(sfile.split('/')[0:-1])+'/'
            sname = sfile.split('/')[-1].split('.chrchr')[0]
            new_flist = glob.glob(loc+sname+'*.txt.gz')
            print (stype,spe,sname,len(new_flist))
            for new_sfile in new_flist:
                new_sname = new_sfile.split('/')[-1].split('.txt.gz')[0]
                with open(out_sh_dir+new_sname+'.sh','w') as fout:
                    systemstr = "zcat "+new_sfile+" | awk '{print $4"+'"/"$4+$5}'+"' > "+out_file_dir+stype+'/'+spe+'/'+new_sname+'.meth'
                    fout.write(systemstr)
            run_systemstr = 'echo "cd '+wd+' && source activate DSS && '
            run_systemstr = run_systemstr + 'python2 multi_run_sh.py '+out_sh_dir+sname
            run_systemstr = run_systemstr+'" | qsub -N '+sname+' -q bioforce-6 -l nodes=1:ppn=6,walltime=10:00:00,mem=32gb'
            print (run_systemstr)
            os.system(run_systemstr)
        for new_sfile in new_flist:
            new_sname = new_sfile.split('/')[-1].split('.txt.gz')[0]
            chr_index = new_sname.split('.chr')[-1].split('.')[0]
            with open(out_sh_dir+spe+'_'+stype+'_'+chr_index+'.sh','w') as fout:
                new_systemstr = "zcat "+new_sfile+" | awk -v OFS='\\t' '{print $1,$2-1,$2}' > "+out_file_dir+stype+'/'+spe+'/'+spe+'_'+stype+'.chr'+chr_index+'.bed'
                fout.write(new_systemstr)
        new_run_systemstr = 'echo "cd '+wd+' && source activate DSS && '
        new_run_systemstr = new_run_systemstr + 'python2 multi_run_sh.py '+out_sh_dir+spe+'_'+stype
        new_run_systemstr = new_run_systemstr+'" | qsub -N '+spe+'_'+stype+' -q bioforce-6 -l nodes=1:ppn=6,walltime=10:00:00,mem=32gb'
        print (new_run_systemstr)
        os.system(new_run_systemstr)

