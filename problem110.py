# prime upto 14 bcz  3**15>8*10**6
# prime 

"""
it base on assumptions number divides 3,5,7,11

"""

import math
limit = 15000
ref = int(math.log(2*limit, 3))+1
print(ref)
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,41,43,47][:ref+1]
def f(n):
    while(n%3==0):
        n//=3
    while(n%5==0):
        n//=5
    while(n%7==0):
        n//=7
    while(n%11==0):
        n//=11
    return True if n==1 else False
minimum = -1
counter = 3**ref - 2*limit
for i in range(13365,3**ref,2):
    if f(i) :
        n=i
        power = []
        ref_counter = 1
        for k in prime[1:]:
            while(n%k==0):
                n//=k
                power.append((k-1)//2)
                ref_counter*=k
        #print(ref_counter)
        if n!=1 or (ref_counter+1)/2<= limit :
            continue
        power.sort(reverse = True)
        sss = prime[:len(power)]
        num = 1
        for pri, po in zip(sss, power):
            num *=pri**po
            # print(f"{pri} ** {po}")
        minimum = num if minimum==-1 else min(minimum, num)
        # minimum.append((num,i, power, (ref_counter+1)/2))
print(minimum)
