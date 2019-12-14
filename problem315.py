digit = {# 0,1,2,3,4,5,6
        0:[[1,1,1,1,1,1,0]],
        1:[[0,1,1,0,0,0,0]],
        2:[[1,1,0,1,1,0,1]],
        3:[[1,1,1,1,0,0,1]],
        4:[[0,1,1,0,0,1,1]],
        5:[[1,0,1,1,0,1,1]],
        6:[[1,0,1,1,1,1,1]],
        7:[[1,1,1,0,0,1,0]],
        8:[[1,1,1,1,1,1,1]],
        9:[[1,1,1,1,0,1,1]], 
        }

# conversion[i][j] means cost of convertion from i to j
conversion = []
for num in range(10):
    ref = [0]*10
    for i in range(10):
        for j in range(7):
            ref[i]+=digit[num][0][j]^digit[i][0][j]
    conversion.append(ref)

for i in range(10):
    digit[i].append(digit[i][0].count(1))
#import pprint
#pprint.PrettyPrinter(indent=2).pprint(conversion)
#pprint.PrettyPrinter(indent=2).pprint(digit)
# 7 to 2 
total = 0 
"""
# calculate prime upto 4475 ==(2*10**7)**0.5 
ref = [1]*4475
prime = []
p = 2
while p<4475:
    if ref[p]==1:
        prime.append(p)
        for i in range(p*p, 4475,p):
            ref[i]=0
    p+=1
ref.clear()
import math as m 
def checkPrime(num):
    temp = m.sqrt(num)
    for i in prime:
        if i>temp:
            return True
        if num%i == 0:
            return False 
    return True
with open("prime_for_problem315",'w') as f:
    for i in range(10**7+1, 2*10**7,2):
        if checkPrime(i):
            f.write(str(i)+'\n')
"""
result=0
l = [-1,-1,-1,-1]
with open("prime_for_problem315",'r') as f:
    for ref in f.readlines():
        ref = int(ref)
        i=0
        l[i]=ref 
        l[1],l[2],l[3]=-1,-1,-1
        i+=1
        while(True):
            total = 0
            s = l[i-1]
            while(s!=0):
                total +=s%10
                s//=10
            l[i]=total 
            i+=1
            if total<10:
                break
        for i in range(4):
            #if l[i]==-1 
            if l[i]==-1:
                break 
            #for sam 
            s= l[i]
            ref = 0
            while(s!=0):
                ref+=digit[s%10][1]
                s//=10
            result+= 2*ref 
            # for max 
            if i==0:
                result-=ref 
            else:
                # if l[i] is last value then add cost of off 
                if i==3 or l[i+1]==-1:
                    result-=ref
                ref1=l[i-1]
                s = l[i]
                ref = 0
                while(s!=0):
                    ref+=conversion[ref1%10][s%10]
                    ref1//=10
                    s//=10
                while(ref1!=0):
                    ref+=digit[ref1%10][1]
                    ref1//=10
                result-=ref 
print(result)
