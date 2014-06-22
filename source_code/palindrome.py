s="malayalam"
print 'YES' if s.lower()==s[::-1].lower() else 'NO'
s="not plain"
print 'YES' if s.lower()==s[::-1].lower() else 'NO'
k=['malayalam','racecar','nopalin']
print map((lambda x:'YES : '+x if x==x[::-1] else 'NO : '+x),k)

