from multiprocessing import Process, Queue
import multiprocessing as mp
from multiprocessing import Pool
import os
import time
import glob


def md5sum(sFile) : 
    return os.popen("CertUtil -hashfile \"{0}\" MD5".format(sFile)).read().split("\n")[0:2]


if __name__ == "__main__":
    # num of multiprocess
    n_process = 16
    p = Pool(n_process)
    lsFile = glob.glob("C:\\Users\\신종환\\Downloads\\**", recursive = True)
    #print(lsFile)

    # queue
    q = Queue()
    n_tmp = 0
    lsQueue_tmp = []
    for i in range(0, len(lsFile), n_process) :      # qeueue init
        while i + n_tmp < len(lsFile) and n_tmp < n_process : 
            lsQueue_tmp.append(lsFile[i])
            n_tmp += 1
        else : 
            q.put(lsQueue_tmp)
            print(lsQueue_tmp)
            lsQueue_tmp = []
            n_tmp = 0

    while not q.empty():
        item = q.get()
        ret = p.map_async(md5sum, item)
        print("is 'ret' ready? :",ret.ready())
        print(ret.get())
        
    print("MainProcess End")
    
