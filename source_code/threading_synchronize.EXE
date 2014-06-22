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
        printElement(self.TName,self.counter,5)
        print "Ending thread : "+self.TName+" ID: " +str(self.threadID)
        
def printElement(threadName, delay, counter):
    while(counter):
        if exitFlag:
            thread.exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter-=1



T1=MyThread(1,"Thread-1",1)
T2=MyThread(2,"Thread-2",2)
T1.start()
T2.start()  
