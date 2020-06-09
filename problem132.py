"""
843296

real    0m1.279s
user    0m1.267s
sys 0m0.012s


R(11) = 2
but 11 also divide A(2*n) n any integer
so simple loop for each prime calculate A() minimum then check 10**9%R(n) == 0 or not

"""
from Project_euler.prime import prime
limit = 10**6
check = 10**9
total=0
p = prime(limit)
count=0
for number in p[3:]:
    totient = number-1
    minimum = totient # totient value
    for j in range(2,int(totient**0.5)+1):
        if totient%j==0:
            if pow(10,j,number)==1:
                minimum = j
                break
            if pow(10,totient//j,number)==1:
                minimum=min(minimum,totient//j)
    if check%minimum==0:
        total+=number
        count+=1
    if count==40:
        break
print(total)