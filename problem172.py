"""
real 0m0.075s
user 0m0.069s
sys 0m0.004s


"""



from collections import Counter

cache = {}
c = Counter()
for i in range(10):
    c[i]+=3

total = 0
def calculate(counter, num_digits, isFirst):
    global total,cache
    if num_digits == 0:
        return 1

    # cache dp here from 1 to 9 count metters bcz genration 
    temp = str(num_digits)+" "+str(counter[0])+" "+" ".join(sorted(str(counter[x]) for x in range(1,10)))
    if temp in cache:
        # print(total)
        total+=1
        return cache[temp]


    res = 0
    for i in range(10):
        if (i==0 and isFirst) or counter[i]==0:
            continue
        counter[i]-=1
        res+=(calculate(counter,num_digits-1,False))
        res%=10**7+7
        counter[i]+=1
    cache[temp] = res
    return res

print(calculate(c,30,True))

