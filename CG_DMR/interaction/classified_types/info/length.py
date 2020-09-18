import sys,glob,os
flist = glob.glob("*.txt")
for sfile in flist:
    print (sfile.split('/')[-1],os.popen("cat "+sfile+" | awk -F \"\t\" 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'").read().strip())

