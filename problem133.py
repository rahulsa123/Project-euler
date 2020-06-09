"""
453647705

real    0m0.675s
user    0m0.667s
sys 0m0.008s



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

for this problem we knew n is prime, i used 10**(k mod totient(n))   



"""
limit = 100000
l=[x for x in range(limit)]

for i in range(2,limit,2):
    l[i]=0
for i in range(5,limit,5):
    l[i]=0
for i in range(3,limit,3):
    l[i] = 0
total = 2+5+3
count = 0


for i in range(7,limit,2):
    if l[i]==0:
        continue
    if l[i]==i:
        # prime
        l[i]=(i-1)
        for j in range(i*i,limit,i):
            l[j]=0
    
        number = i
        totient = (l[i])
        minimum = totient
        for j in range(2,int(totient**0.5)+1):
            if totient%j==0:
                if pow(10,j,number)==1:
                    minimum = j
                    break
                if pow(10,totient//j,number)==1:
                    minimum=min(minimum,totient//j)
        while minimum%2==0:
            minimum//=2
        while minimum%5==0:
            minimum//=5
        if minimum!=1:
            total+=i
print(total)