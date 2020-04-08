first =["","one", "two", "three", "four", "five", "six", "seven", "eight", "nine","ten","eleven","twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
second =["twenty", "thirty", "forty", "fifty", "sixty","seventy", "eighty", "ninety"]
third = ["hundred", "thousand"]

n,m = [int(x) for x in input().split()]
def less20(ref):
    return first[ref]
def less100(ref):
    return second[ref//10-2]+first[ref%10]
def getname(n):
    s=""
    if(n>999):
        if(n//1000<20):
            s+=less20(n//1000)
        elif(n//1000<100):
            s+=less100(n//1000)
        s+=third[1]
        n%=1000
    if(n>99):
        if n//100!=0:
            s+=first[n//100]+third[0]
        n%=100
        if(n!=0):
            s+="and"
    if(n>19):
        s+=second[n//10 -2]
        n%=10
    if(n!=0):
        s+=less20(n)
    return s
h=0
for i in range(1,1001):
    h+=len(getname(i))
print(h)


