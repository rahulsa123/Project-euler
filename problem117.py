"""
dp with array

real    0m0.063s
user    0m0.031s
sys 0m0.004s

"""
block = 50
result = [0]*(block+1)
def calculate(block):
    global result
    if result[block]!=0:
        return result[block]
    total = 0
    if block == 0:
        return 1
    if block>=1:
        total+= calculate(block-1)
    if block>=2:
        total+= calculate(block-2)
    if block>=3:
        total+= calculate(block-3)
    if block>=4:
        total+= calculate(block-4)
    result[block] = total
    return total

print(calculate(block))