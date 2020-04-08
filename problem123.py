def remainder(a,b,c):
    res = 1
    a = divmod(a,c)[1]
    while b>0:
        if divmod(b,2)[1]==1:
            res = divmod(res*a,c)[1]
        b//=2
        a = divmod(a*a,c)[1]
    return res
from primeupto import prime
for power, pri in enumerate(prime(10**6)):
    ref = remainder(pri-1, power+1,pri**2)+remainder(pri+1, power+1,pri**2)
    if ref%(pri**2)>10**10:
        print(power+1)
        exit()
