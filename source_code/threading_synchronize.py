try:
    import threading
    import time
except ImportError:
    print "Import Error"
    
exitFlag=0
class MyThread(threading.Thread):
    def __init__(self,threadID,TName,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.TName=TName
        self.counter=counter
    def run(self):
        print "Starting thread : "+self.TName+" ID: " +str(self.threadID)
        print "Acquiring threadLock",threadLock.acquire()
        printElement(self.TName,self.counter,5)
        print "Releasing threadLock" ,  threadLock.release()
        print "Ending thread : "+self.TName+" ID: " +str(self.threadID)
        
def printElement(threadName, delay, counter):
    while(counter):
        if exitFlag:
            thread.exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter-=1

threadLock=threading.Lock()

T1=MyThread(1,"Thread-1",1)
T2=MyThread(2,"Thread-2",2)
#Staring the threads
T1.start()
T2.start()

threads=[]
threads.append(T1)
threads.append(T2)

#Waiting for the threads to complete
for t in threads:
    t.join()
    print "Joining threads"

print "Exiting main thread"
