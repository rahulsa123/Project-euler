# num: [incresing, decresing]
digit = {
    1: [9, 2],
    2: [8, 3],
    3: [7, 4],
    4: [6, 5],
    5: [5, 6],
    6: [4, 7],
    7: [3, 8],
    8: [2, 9],
    9: [1, 10],
}
bouncy = 0
limit  = 100
for zeros in range(3, limit+1):
    for num in range(1, 10):
        # for incresing
        if 10-num-1 > 0:
            digit[10-num-1][0] += digit[10-num][0]
        # for decresing
        if num == 1:
            digit[num][1]+=1
        else:
            digit[num][1]+=digit[num-1][1]
    ref = sum([sum(digit[x]) for x in digit ])
    bouncy+= (9*10**(zeros-1) -ref + 9)
print(int("9"*limit)-bouncy)
