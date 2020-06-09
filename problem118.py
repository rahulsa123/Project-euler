"""
44680

real    4m34.562s
user    4m34.477s
sys 0m0.040s

"""
import itertools
from Project_euler.prime import is_prime
s = []
for i in range(1,10):
    print(i)
    for num in itertools.permutations("135792468",i):
        if len(num)>1 and int(num[-1])%2==0:
            continue
        temp = ""
        for ref in num:
            temp+=ref
        # print(temp)
        temp = int(temp)
        if is_prime(temp):
            s.append(temp)
total=0
def calculate(index, ref, temp):
    global total
    if all(ref):
        total+=1
        return
    if index>=len(s) or ref.count(False)<len(str(s[index])):
        return
    for i in range(index,len(s)):
        # means not digit found till this point
        if all(not ref[int(x)] for x in str(s[i])):
            # mark those digit as True
            for j in map(int,str(s[i])):
                ref[j]=True
            calculate(i+1,ref, temp+str(s[i])+" ")
            # unmark those digit as False
            for j in map(int,str(s[i])):
                ref[j]=False




calculate(index=0, ref=[True]+[False]*9, temp=" ")
print(total)