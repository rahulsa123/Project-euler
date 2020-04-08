l={1}
for base in range(2,10**6+1):
    s = 1+base 
    power = 2 
    while(s+base**power<10**12):
        l.add(s+base**power)
        s+=base**power 
        power+=1 
print(sum(l))
