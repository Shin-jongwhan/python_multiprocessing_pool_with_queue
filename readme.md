# 221122

## python - multiprocessing, queue 와 pool 을 함께 쓰는 방법
### <br/><br/><br/>

```
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
```
### <br/><br/><br/>

### 결과
#### 설정한 값 대로 pool 개수가 구성된 것대로 리스트로 출력이 되었다.
#### ![image](https://user-images.githubusercontent.com/62974484/203234244-d25ac628-596e-42f4-a25b-1a4e2b20b2e1.png)
