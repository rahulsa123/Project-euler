# prime upto 14 bcz  3**15>8*10**6
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,41,43]
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
for i in range(8*10**6+1,9*10**6):
    if f(i):
        n=i
        break
power = []
while(n%3==0):
    n//=3
    power.append(1)
while(n%5==0):
    n//=5
    power.append(2)
while(n%7==0):
    n//=7
    power.append(3)
while(n%11==0):
    n//=11
    power.append(4)
power.sort(reverse = True)
prime = prime[:len(power)]
num = 1
for pri, po in zip(prime, power):
    num *=pri**po
print(num)

