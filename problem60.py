import math
from array import array

PRIMES = array("b", [1]*10000)
limit = len(PRIMES)**0.5
cur = 2
first = True
PRIMES[0] = 0
PRIMES[1] = 0
def cal_prime():
    global cur, first
    while cur<=limit:
        if PRIMES[cur]==1:
#            print("prie",cur)
            for i in range(cur*cur, len(PRIMES), cur):
                PRIMES[i] = 0
        if first:
            cur += 1
            first = False
        else:
            cur += 2
cal_prime()
l= [2,3]
for i in range(5, 10000, 2):
    if PRIMES[i]==1:
        l.append(i)
#print(l)
def checkp(num1, num2):
    test1 = num1*10**(math.ceil(math.log10(num2)))+num2
    test2 = num2*10**(math.ceil(math.log10(num1)))+num1
    test = max(test1, test2)
    if test<len(PRIMES):
        if PRIMES[test1]==1 and PRIMES[test2]==1:
            return True
        return False
    if test1 % 2 == 0 or test2%2==0:
        return False
    sqrt_n = int(math.floor(math.sqrt(test)))
    for i in l:
        if i>sqrt_n:
            break
        if test1 % i == 0 or test2%i==0:
            return False
    return True

for i1 in range(len(l)):
    for i2 in range(i1+1,len(l)):
        if not checkp(l[i1], l[i2]):
            continue
        for i3 in range(i2+1,len(l)):
            if not (checkp(l[i1], l[i3]) and checkp(l[i2], l[i3])):
                continue
            for i4 in range(i3+1,len(l)):
                if not (checkp(l[i1], l[i4]) and checkp(l[i2], l[i4]) and checkp(l[i3], l[i4])):
                    continue
                for i5 in range(i4+1,len(l)):
                    if not (checkp(l[i1], l[i5]) and checkp(l[i2], l[i5]) and checkp(l[i3], l[i5]) and checkp(l[i4], l[i5])):
                        continue
                    print(l[i1], l[i2], l[i3], l[i4], l[i5])
                    exit()
