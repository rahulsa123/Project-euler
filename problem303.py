"""
real    0m17.025s
user    0m16.506s
sys 0m0.516s



        1s followed by  2s
9       1               4
99      2               8
999     3               12
9999    4               16

11112222222222222222 /9999 == 1111333355557778
"""
import collections
test = {"1","2","0"}
def calculate(num, testing):
    minimum = -1
    #print(len(testing))
    for values in testing:
        rem, qu = values
        if len(set(str(rem)).union(test))==3:
            if minimum== -1 or minimum>int(qu):
                minimum = int(qu)
    if minimum!=-1:
        return minimum
    ref = collections.deque()
    for values in testing:
        rem, qu = values
        for i in range(0,10):
            if (num*i + rem)%10<=2:
                ref.append(((num*i + rem)//10, str(i)+qu))

    return calculate(num, ref)

total=0
total+= 1111333355557778 # for 9999
total+= 1
for num in range(1,9999):
    ref = []
    for i in range(1,10):
        if (num * i)%10<=2:
            ref.append(((num*i)//10, str(i)))
    t = calculate(num, ref)
    # print(num,t)
    total+=t
print(total)
