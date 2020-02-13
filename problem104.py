import math as m 
phi = m.log10(5**0.5+1)-m.log10(2)
sq = 0.5*m.log10(5)
f1,f2 = 1,1
count = 3
s = {x for x in "123456789"}
while(True):
    f1,f2 = f2,(f1+f2)%(10**9)
    if set(str(10**m.modf((count*phi-sq))[0]*10**9)[:9])==s and set(str(f2))==s:
        print(count)
        break
    count+=1
