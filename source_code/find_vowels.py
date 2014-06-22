import collections
s=' How do you remove duplicates'
k=[x for x in s.lower() if x in 'aeiou']
print k
for x,y in collections.Counter(k).items():
	print x,y
