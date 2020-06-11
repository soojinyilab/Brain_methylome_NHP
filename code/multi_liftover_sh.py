import sys,glob
import os
import Queue,threading

class ThreadRBH(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while True:
            systemstr = self.queue.get()
            print (systemstr)
            os.system(systemstr)
            self.queue.task_done()

exe_list = []
with open(sys.argv[1],'r') as fp:
    for line in fp:
        exe_list.append(line.strip())

queue = Queue.Queue()
for i in range(4):
    t = ThreadRBH(queue)
    t.setDaemon(True)
    t.start()
for exes in exe_list:
    queue.put(exes)
queue.join()

'''
(liftover) [hjeong84@login-s2 code]$ more ../2_lifted_over_cytosine/CH/tmp/tmp_sh/split_liftover_input_Macaq_CH.sh.bu
liftOver ../2_lifted_over_cytosine/CH/tmp/split_Macaq_OD_CH.gc /nv/hp10/hjeong84/data/references/human/liftOver/rheMac8ToHg19.over.chain ../2_lifted_over_cytosine/CH/tmp/tmp_hg19/split_hg19_Macaq_OD_CH.gc ../2_
lifted_over_cytosine/CH/tmp/tmp_hg19/unmapped/split_unmapped_Macaq_OD_CH.gc
liftOver ../2_lifted_over_cytosine/CH/tmp/split_Macaq_ND_CH.en /nv/hp10/hjeong84/data/references/human/liftOver/rheMac8ToHg19.over.chain ../2_lifted_over_cytosine/CH/tmp/tmp_hg19/split_hg19_Macaq_ND_CH.en ../2_
lifted_over_cytosine/CH/tmp/tmp_hg19/unmapped/split_unmapped_Macaq_ND_CH.en
liftOver ../2_lifted_over_cytosine/CH/tmp/split_Macaq_ND_CH.fv /nv/hp10/hjeong84/data/references/human/liftOver/rheMac8ToHg19.over.chain ../2_lifted_over_cytosine/CH/tmp/tmp_hg19/split_hg19_Macaq_ND_CH.fv ../2_
lifted_over_cytosine/CH/tmp/tmp_hg19/unmapped/split_unmapped_Macaq_ND_CH.fv
liftOver ../2_lifted_over_cytosine/CH/tmp/split_Macaq_ND_CH.ft /nv/hp10/hjeong84/data/references/human/liftOver/rheMac8ToHg19.over.chain ../2_lifted_over_cytosine/CH/tmp/tmp_hg19/split_hg19_Macaq_ND_CH.ft ../2_
lifted_over_cytosine/CH/tmp/tmp_hg19/unmapped/split_unmapped_Macaq_ND_CH.ft
'''
