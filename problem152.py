# import fractions
# ref = [[fractions.Fraction(1, x**2), fractions.Fraction(0, 1)]
#        for x in range(2, 46)]

# for i in range(len(ref)-2, -1, -1):
#     ref[i][1] += ref[i+1][1]+ref[i+1][0]

# result = 0
# equal = fractions.Fraction(1, 2)


# def calculate(index, temp, test):
#     global equal, result
#     # check temp == 1/2 or not
#     if index >= len(ref):
#         return
#     if temp == equal:
#         result += 1
#         print(test)
#         return

#     # first add element iff temp+current[0] <= equal and
#     #  equal-(temp+current[0]) <= curr[1]
#     if temp + ref[index][0] <= equal and \
#             equal-(temp+ref[index][0]) <= ref[index][1]:
#         calculate(index+1, temp+ref[index][0],
#                   test+str((ref[index][0].denominator)**0.5)+" ")

#     # second not taking current element
#     # iff equal - temp <= current[1]
#     if temp <= equal and equal-temp <= ref[index][1]:
#         calculate(index+1, temp, test)


# calculate(index=0, temp=fractions.Fraction(0, 1), test="")
# print(result)

from prime import prime
from collections import Counter
primes = prime(45)
numbers = {}
for num in range(2,46):
    number = Counter()
    temp = num
    for i in primes:
        if(temp==1):
            break
        if(temp%i==0):
            iPower = 0
            while(temp%i==0):
                iPower += 1
                temp//=i
            number[i] = 2*iPower
    numbers[num**2] = number