"""
dp with array
using loop for block size
real    0m0.166s
user    0m0.142s
sys 0m0.000s



"""
m=50
block = 50
while True:
    result = [0]*(block+1)
    def calculate(block):
        global result
        total = 0
        if result[block]!=0:
            return result[block]
        if block <= 0:
            return 1
        if block>=1:
            total+=calculate(block-1)
        for i in range(m,block+1):
            if block>=i:
                total+=calculate(block-i-1)
        result[block] = total
        return total
    if calculate(block)>10**6:
        print(block)
        break
    block+=1