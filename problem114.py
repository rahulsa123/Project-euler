"""
dp with array
using loop for making more than 3 condition
rreal   0m0.111s
user    0m0.027s
sys 0m0.009s


"""
block = 50
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
    for i in range(3,block+1):
        if block>=i:
            total+=calculate(block-i-1)
    result[block] = total
    return total

print(calculate(block))