"""
simple method make all equations then remove recursively last element at he end you get solution

"""

import time 
tt= time.time()
z = [1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10 for n in range(1,11+1)]
ss=0
for i in range(len(z)-1):
    term = z[:i+1]
    n = [x for x in range(1,len(term)+1)]
    # [[a,b,c,d],result] 
    #a,b,c,d
    result =[None]*len(term)
    equation = []
    for nth,val in zip(n,term):
        equation.append([[nth**i for i in range(len(n))],val])
        equation[-1][0].reverse()
    import math as m
    import copy 
    while(result.count(None)>0):
        eq = copy.deepcopy(equation)
        while(len(eq[0][0])!=1):
            # get lcm of each quation last element
            number = eq[0][0][-1]
            for i in range(1,len(eq)):
                gcd = m.gcd(number,eq[i][0][-1])
                number*=eq[i][0][-1]
                number//=gcd
                
            # now multiplay number/ eq[i][0][-1] to each ellement in equation and also vale 
            for i in range(len(eq)):
                ref = number//eq[i][0][-1] 
                for indx in range(len(eq[i][0])):
                    eq[i][0][indx]*=ref
                eq[i][1]*=ref
            
            for i in range(1, len(eq)):
                eq[i][1]-=eq[0][1]
                for indx in range(len(eq[i][0])):
                    eq[i][0][indx]-=eq[0][0][indx]
                #remove last element of equation
                eq[i][0] = eq[i][0][:len(eq[i][0])-1]
            # now remove first equation
            eq = eq[1:]
            
        get_value=eq[0][1]/eq[0][0][0]
        result[result.index(None)]=get_value
        # now multiply this value with first element of equation and sub with val and remove it 
        # from eq 
        for i in range(len(equation)):
            t = equation[i][0][0]*get_value
            equation[i][1]-=t
            equation[i][0] = equation[i][0][1:]
    next_term = 0
    result.reverse()
    place = n[-1]+1
    for i in range(len(result)):
        next_term +=result[i]*(place**i)
    print(next_term)
    ss+=next_term 
print(ss, time.time()-tt)
