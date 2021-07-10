total = 0
from collections import Counter
c = Counter()
hash_table = Counter()

# print("dd")
# exit()
def calculate(curr_prev, curr_prev_prev, num_digits, isFirst):
    if num_digits == 0:
        return 1

    hash = num_digits*100 + curr_prev_prev*10+ curr_prev
    if hash_table[hash]!=0:
        return hash_table[hash]

    result = 0
    curr = 0
    while(curr+curr_prev+curr_prev_prev<=9):
        if curr == 0 and isFirst:
            curr += 1
            continue
        result += calculate(curr, curr_prev, num_digits-1, False)
        curr += 1

    hash_table[hash] = result
    # print(result)
    return result


print(calculate(0,0,20,True))


# import pprint
# pp = pprint.PrettyPrinter()
# print(pp.pprint(c))