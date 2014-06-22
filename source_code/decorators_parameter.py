def wrap_up(a,b):
    print "In wrap_up : ",a,b
    def wrapper_out(func):
        print "In wrapper_out : ",a,b
        def wrapper(c,d):
            print "In wrapper : ",a,b,c,d
            func(c,d)
            print "End wrapper : ",a,b,c,d
        print "End wrapper_out : ",a,b
        return wrapper
    print "End wrap_up : ",a,b
    return wrapper_out


@wrap_up("sam","Mike")
def impl_warp(a,b):
    print "The function works {0} & {1}".format(a,b)    

impl_warp('pike','andy')

impl_warp('k','f')

#wr=wrap_up('sam','katie')
#p=wr(impl_warp)
#print p(1,2)

