import time 
found = 0
perfact = 0
def powerof2(x):
    return (x and (not(x & (x - 1)))) 
m=1
t = time.time()
while(True):
    if powerof2(m+1):
        perfact+=1
    found+=1
    if perfact*12345<found:
        print(m*(m+1),time.time()-t)
        break 
    m+=1
