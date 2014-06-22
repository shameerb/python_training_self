def test(&a):
    print "within test :",a
    a=5
    print "within test after changing :",a

b=2
print "in main ",b
test(b)
print "in  main after call: ",b
