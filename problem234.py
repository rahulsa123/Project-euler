"""
1259187438574927161

real    0m8.200s
user    0m8.190s
sys 0m0.008s

"""
from prime import prime
limit = 999966663333
prime = prime(int(limit**0.5)+10)
c=1
total = 0
maximum = 0 
def calculate(p1,p2,lower_limit, upper_limit):
    global maximum
    p1_mul = p1+1
    p2_mul = lower_limit//p2+1
    count = 0
    ref = p1*p2
    while True:
        minimum = 0
        if p1_mul*p1<p2_mul*p2:
            minimum = p1_mul*p1
            p1_mul+=1
        elif p1_mul*p1>p2_mul*p2:
            if p2_mul==p2:
                return count
            minimum = p2_mul*p2
            p2_mul+=1
        else:
            minimum = p2_mul*p2
            p1_mul+=1
            p2_mul+=1
        if   minimum>upper_limit:
            return count
        if minimum%ref!=0:
            count+=minimum
            maximum = max(maximum,minimum)
total = 0
for i in range(1,len(prime)):
    p1,p2 = prime[i-1], prime[i]  # p1=2 p2=3

    lower_limit, upper_limit = p1**2, p2**2
    if lower_limit>limit:
        break
    
    upper_limit = min(upper_limit,limit)
    total+=calculate(p1,p2,lower_limit,upper_limit)
print(total)



