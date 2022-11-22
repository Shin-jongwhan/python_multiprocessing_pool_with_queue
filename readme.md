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
    time.sleep(3)
    return os.popen("CertUtil -hashfile \"{0}\" MD5".format(sFile)).read().split("\n")[0:2]


if __name__ == "__main__":
    # num of multiprocess
    n_process = 12
    p = Pool(n_process)
    lsFile = glob.glob("C:\\Users\\신종환\\Downloads\\**", recursive = True)
    #print(lsFile)
    
    # queue
    q = Queue()
    n_tmp = 0
    lsQueue_tmp = []
    for i in range(0, len(lsFile), n_process) :      # queue init
        while i + n_tmp < len(lsFile) and n_tmp < n_process : 
            lsQueue_tmp.append(lsFile[i + n_tmp])
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
        print(ret.get())        # wait until all jobs finished
        
    print("MainProcess End")
    
```
### <br/><br/><br/>

### 결과
#### 설정한 값 대로 pool 개수가 구성된 것대로 리스트로 출력이 되었다.
#### ![image](https://user-images.githubusercontent.com/62974484/203247583-b9a2f998-2d3a-461d-a1ac-2378ceb57184.png)

