"""
1000023

real    0m0.285s
user    0m0.255s
sys 0m0.028s


R(k) =  10**k - 1  
       -----------
            9      

for any n where gcd(n,10)== 1
R(k) mod n == 0
 (10**k - 1 mod n*9) = 0  

1 mod n*9 == 1
so 10**k mod n*9 must equal to 1 then 1-1 ==0
10**k mod n**9 == 1
now here i applied totient remainder theorem, 10**(k mod totient(n*9)) because gcd(10,n*9)==1

so k must be in range from 1 to totient(n*9) here one more point, must be a factor of totient(n*9)  

"""
from Project_euler.prime import prime
import math
p = prime(1500000)
p.remove(2)
p.remove(5)
p = set(p)
start = 10**6+1
while True:
    # pass all the unwanted case
    if math.gcd(start,10)!=1:
        start+=1
        continue
    # calculate totient value
    totient,ref = start*9,start*9
    for i in p:
        if ref%i==0:
            totient*=(i-1)
            totient//=i
            ref//=i
            while ref%i==0:
                ref//=i
            if ref==1:
                break
    minimum = totient
    for i in range(2,int(totient**0.5)+1):
        if totient%i==0:
            if pow(10,i,start*9)==0:
                minimum = i
                break
            if pow(10,totient//i,start*9)==1:
                minimum=min(minimum,totient//i)
    if minimum>10**6:
        print(start)
        break
    start+=1