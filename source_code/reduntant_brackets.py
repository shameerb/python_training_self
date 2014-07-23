length=0
'''start=0
end=0
pos_dict={'(':[],')':[]}
def check_brackets(s,start,end):
    global pos_dict
    s_pos=s.find("(",start,end)
    e_pos=s.rfind(")",start,end)
    s=s
    while(s_pos!=-1 or e_pos!=-1):
        pos_dict[')'].append(s_pos)
        pos_dict['('].append(e_pos)
        s=s[s_pos:e_pos]
        print s
        s_pos=s.find("(",s_pos,e_pos)
        e_pos=s.rfind(")",s_pos,e_pos)    
    
    #if(s_pos!=-1):
        
    print s[s_pos+1:e_pos-1]
    
    print s_pos,e_pos
    return s_pos



s="((a*b+(c+d)*e+(f+g)+((e*c)*(e+c))))"
length=len(s)
end=length
k=check_brackets(s,start,end)
print pos_dict
#print s[0:3]'''

def check_bracket(sub,l_start,r_start):
    global length
    reduntant=True
    h_p,l_p=0,0
    #print "init",h_p,l_p
    for val in sub[1:-1] :
        if val in ['*']:
            h_p+=1
     #       print h_p
        elif val in ['+','-']:
            l_p+=1
      #      print l_p
    #print "After for",h_p,l_p
    if l_p > 0 and h_p > 0:
        reduntant=False

    #print reduntant
    if reduntant is True and l_start+1 != length:
        lhs=s[r_start-1]
        rhs=s[l_start+1]
     #   print "lhs: ",lhs,"rhs",rhs
      #  print "After for",h_p,l_p
        for val in [lhs,rhs]:
       #     print val
            if val in ['*']:
                if l_p > 0:
                    reduntant=False
            

    #print reduntant
    return reduntant

def change_string(l_start_prev,r_start_prev,s):
    #print 30*"*"
    #print s
    l_start=s.find(')',l_start_prev+1)
    r_start=s.rfind('(',0,l_start)
    #print l_start,r_start
    sub=s[r_start:l_start+1]
    #print "substring2",sub
    if check_bracket(sub,l_start,r_start):
        #print "pattern",s,sub
        s=s[:r_start]+"!"+s[r_start+1:l_start]+"!"+s[l_start+1:]
    else:
        #print "pattern",s,sub
        s=s[:r_start]+'<'+s[r_start+1:l_start]+'>'+s[l_start+1:]
    return l_start,r_start,s

def remove_bracket(s):
    global length
    length=len(s)
    #print length
    l_start,r_start=0,0

    while l_start+1 != length:
        l_start,r_start,s=change_string(l_start,r_start,s)
        

    #print s
        
    s=s.replace('<','(')
    s=s.replace('>',')')
    s=s.replace('!','')
    return s


s="((a*b+(c+d)+e*(f+g)+((e*c)+(e*c))))"
#s="((a*b*(c*d)*e*(f*g)*((e*c)*(e*c))))"
p=remove_bracket(s)
print s
print p
        
