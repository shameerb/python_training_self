try:
    import thread
    import time
    import random
except ImportError,e:
    print "Could not import module :",e

def runt(TName,timeSleep):
    while True:
        time.sleep(timeSleep)
        print "Thread running %s "%TName

if __name__=="__main__":
    try:
        thread.start_new_thread(runt,('Fast',1))
        thread.start_new_thread(runt,('Slow',3))
        thread.start_new_thread(runt,('Random',(random.random())))
    except Exception ,e:
        print str(e)
    
