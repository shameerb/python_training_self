from itertools import count

def create_prime(stop_at=0):
    prime=[]
    
    for i in count(2):
        if 0<stop_at<i:
            return
        composite=False
        for k in prime:
            if not i%k:
                composite=True
                break
        if not composite:
           prime.append(i)
           yield i
           
for k in create_prime():
    if k > 100 :
        break
    print k
