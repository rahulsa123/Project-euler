"""
126461847755
TotalSeconds      : 0.9815246
"""


prev = [[0]*(2**10) for _ in range(10)]
curr = [[0]*(2**10) for _ in range(10)]


#logic for prev one digit number

for i in range(10):
    prev[i][1<<i]=1
# print(prev[0][1<<0])
# logic for two digit
numDigit = 40
total = 0
for _ in range(numDigit-1):
    for i in range(10): # include zero 01 is useful for 101
        # check all posible number
        for j in range(2**10):
            # i+1
            if i!=9:
                curr[i][(1<<i)|j] += prev[i+1][j]
            # i-1
            if i!=0:
                curr[i][(1<<i)|j] += prev[i-1][j]
        # swap prev and curr AND reset curr
    
    for i in range(10):
        if i!=0:
            total += curr[i][1023] # total number which starts with digit i and contains all number from 0-9
        for j in range(2**10):
            prev[i][j] = curr[i][j]
            curr[i][j]=0
    
# print(sum([sum(prev[i]) for i in range(1,10)]))
print(total)

