def decorate_dec(dec_call):
    print "Decorating Decorators"
    
    def wrap(func):
        return dec_call(func,*args,**kwargs)
    return wrap 
    
    
    
    

@decorate_dec
def wrap_up(func,a,b):
    print "In wrap_up : ",a,b
    def wrapper(c,d):
        print "In wrapper : ",a,b,c,d
        func(c,d)
        print "End wrapper : ",a,b,c,d
    print "End wrapper_out : ",a,b
    return wrapper
    print "End wrap_up : ",a,b
    


@wrap_up("sam","Mike")
def impl_warp(a,b):
    print "The function works {0} & {1}".format(a,b)    

impl_warp('pike','andy')

#wr=wrap_up('sam','katie')
#p=wr(impl_warp)
#print p(1,2)

