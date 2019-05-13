import math as m
l =[2,3,5,7]
n=9
def getPrime(n):
    n=n+2
    while(True):
        k=m.sqrt(n)
        for i in l:
            if(i>k):
                l.append(n)
                return n
            else:
                if(n%i==0):
                    n+=2
                    break
su=0
a=l[-1]
for k in range(11):
    res=-1
    while(True):
        a=getPrime(a)
        ref=str(a)
        for i in range(len(ref)-1):
            if(int(ref[:i+1]) not in l):
                break
            if(int(ref[i+1:]) not in l):
                break
        else:
            break
    su+=a
    print(a)
    
print(su)
            
