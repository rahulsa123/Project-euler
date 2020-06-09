"""
149253

real    0m1.670s
user    0m1.583s
sys 0m0.032s


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
l=[x*9 for x in range(10**6)]

for i in range(2,10**6,2):
    l[i]=0
for i in range(5,10**6,5):
    l[i]=0

# for i in range(3,10**6,3):
#     l[i]*=2
#     l[i]//=3
total = 0
count = 0
for i in range(7,10**6,2):
    if l[i]==0:
        continue
    if l[i]==9*i:
        # prime
        l[i]=i-1
        for j in range(2*i,10**6,i):
            l[j]*=(i-1)
            l[j]//=i
    else:
        number = i
        totient = (l[i]*2)//3
        minimum = totient
        for j in range(2,int(totient**0.5)+1):
            if totient%j==0:
                if pow(10,j,number*9)==1:
                    minimum = j
                    break
                if pow(10,totient//j,number*9)==1:
                    minimum=min(minimum,totient//j)
        if (i-1)%minimum==0:
            total+=i
            count+=1
        if count==25:
            print(total)
            break