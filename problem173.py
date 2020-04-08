"""
there are two series of number
l1=8 16 24 32 40
l2=12 20 28 36
using first series
    d=8 a1=8
    now for limit 10**6 list goes upto 125000
using secnod series
    d=8 a1=12
    now for limit 10**6
    10**6 = 12+(n-1)*8
        n= 124998
"""
limit = 10**6
l1 = [8*x  for x in range(1,limit//8+2)]
l2 = [12+(x-1)*8 for x in range(1,(limit-12)//8+2)]
while(l1[-1]>limit):
    l1.pop()
while(l2[-1]>limit):
    l2.pop()
total = len(l1)+len(l2)
def calculate(l):
    global total
    for i in range(len(l)-1):
        if l1[i]+l[i+1]>limit:
            break
        ref = l[i]
        for j in range(i+1,len(l)):
            ref+=l[j]
            if ref>limit:
                break
            total+=1
calculate(l1)
calculate(l2)
print(total)








