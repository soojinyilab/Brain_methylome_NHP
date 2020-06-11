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
flist = glob.glob(sys.argv[1]+"*.sh")
print (flist)
for sfile in flist:
    systemstr = "bash "+sfile
    print (systemstr)
    exe_list.append(systemstr)

queue = Queue.Queue()
for i in range(12):
    t = ThreadRBH(queue)
    t.setDaemon(True)
    t.start()
for exes in exe_list:
    queue.put(exes)
queue.join()

