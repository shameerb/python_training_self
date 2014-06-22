def logger(ar_1):
    def wrapper_out(func):
        def wrapper(*args,**kwargs):
            wrapper.count=wrapper.count+1
            print "LOGGER START"
            res=func(*args,**kwargs)
            print "LOGGER : ",func.__name__,args,kwargs,wrapper.count
            return res
        wrapper.count=0
        return wrapper
    return wrapper_out

def timer(ar_1):
    import time
    def wrapper_out(func):
        def wrapper_time(*args,**kwargs):
            t=time.clock()
            wrapper_time.count=wrapper_time.count+1
            print "TIMER STARTS"
            res=func(*args,**kwargs)
            print "TIMER : ",func.__name__,args,kwargs,wrapper_time.count," Time " ,time.clock()-t
            return res
        wrapper_time.count=0
        return wrapper_time
    return wrapper_out

def nosOfCalls(ar_1):
    def wrapper_out(func):
        def wrapper_calls(*args,**kwargs):
            wrapper_calls.count=wrapper_calls.count+1
            print "CALLS START"
            res=func(*args,**kwargs)
            print "CALLS : ",func.__name__,args,kwargs,wrapper_calls.count
            return res
        wrapper_calls.count=0
        return wrapper_calls
    return wrapper_out


@logger(1)
@timer(2)
@nosOfCalls(3)
def impl_funct(abc):
    return str(abc)

print impl_funct("Shameer")

