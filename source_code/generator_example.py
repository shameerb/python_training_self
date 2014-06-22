def gen():
    for i in range(5):
        print "Shameer"
        yield [i,i+2]

for k in gen():
    print k
    print "Within"

for m in gen():
    print m
