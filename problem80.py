import math as m
def cal(number):
    result=""
    p=m.floor(m.sqrt(number))# p=1
    result+=str(p)
    ref=number-p*p # ref=2-1
    p+=p# 2
    for i in range(100):
#        print(result)
        ref*=100
        while((p*10+1)>ref):
            p*=10
            ref*=100
            result+="0"
        ref2=p*10
        ans=0
       # print("\n",ref,p)
        if(len(result)>100):
            return sum([int(x) for x in result[:100]])
        for i in range(1,10):
            s=(ref2+i)*i
            if(s>ref):
                ans=(i-1)
                result+=str(ans)
                break
        if(ans==0):
            ans=9
            result+="9"
        if(len(result)>100):
            return sum([int(x) for x in result[:100]])
        p=ref2+ans
        ref=ref-p*ans
        p+=ans
    if(len(result)>100):
        return sum([int(x) for x in result])

total=0
for i in range(2,101):
    ref=m.sqrt(i)
    if(ref!=int(ref)):
        ref2=cal(i)
        total+=ref2
        print(i,ref2)
print(total)
