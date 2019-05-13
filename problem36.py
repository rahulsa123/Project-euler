res = 0
for i in range(1,1000000):
    s1=str(i)
    s2=bin(i)[2:]
    if(s1==s1[::-1] and s2 ==s2[::-1]):
        print(i)
        res+=i
        if(i==585):
            print("yes")
print(res,"res")
