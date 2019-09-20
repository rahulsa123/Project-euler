test =[x for _ in range(200000) for x in [False,True]]
test[0]=test[1]=False
l=[2]
p=3
while p*p<=400000:
    if test[p]:
        l.append(p)
        for i in range(p*p,len(test),p):
            test[i]=False
    p+=2
for i in range(p,len(test)):
    if test[i]:
        l.append(i)
def prime(temp):
    ref1= temp**0.5
    for i in l:
        if temp%i==0:
            return False
        if i>ref1:
            return True
s=["0"]*10
ans=0
for i in range(1,10):
    ref=list(s)
#    print(ref)
    ref[0]=str(i)
    for j in range(1,10,2):
        ref[-1]=str(j)
        temp=int("".join([x for x in ref]))
        if prime(temp):
            ans+=temp
            print("0",temp)
print(ans)
d={x:(str(x))*10 for x in range(1,10)}
for ref in d:
    if ref==2 or ref== 8:
        continue
    for index in range(10):
        temp = list(d[ref])
        for value in range(10):
            temp[index]=str(value)
            ref1= int("".join([x for x in temp]))
            if prime(ref1):
                print(ref1)
                ans+=ref1
# for 2 and 8 changing digits are 2
for ref in [2,8]:
    for index1 in range(9):
        for value1 in range(10):
            if index1==0 and value1==0:
                continue
            for index2 in range(index1+1,10):
                for value2 in range(10):
                    temp = list(d[ref])
                    temp[index1]=str(value1)
                    temp[index2]=str(value2)
                    ref1=int("".join([x for x in temp]))
                    if prime(ref1):
                        print(ref1)
                        ans+=ref1
print(ans)








