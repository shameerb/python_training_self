import glob

w=open("write.txt",'a')
for i in glob.glob("*.txt"):
    with open(i) as f:
        w.write(f.read())
        print "written"

w.close()
