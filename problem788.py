"""
100%|███████████████████████████████████████| 2022/2022 [48:17<00:00,  1.43s/it]
1029471752702
"""

import sys

import functools
import tqdm

sys.setrecursionlimit(10**5)


# @functools.lru_cache(maxsize=10**7)
def calculate(left, position):
    global digit
    # ref = str(digit) + "#" + str(left) + "#" + str(position)
    # if ref in memo:

    #     return memo[ref]
    if position == digit + 1 or left == 0:
        return 9

    total = 0

    ref = calculate(left - 1, position + 1)
    # consider this position or
    if position == 1:
        # means we can only place 8 digit here no zero and same num
        total += 8 * ref
        # for zero only#
        total += ref

    else:
        total += 9 * ref

    # don't consider this position
    total += calculate(left, position + 1)
    total %= 10**9 + 7
    # memo[ref] = total
    return total


total = 0
for digit in tqdm.tqdm(range(1, 5)):
    left = int((digit - digit / 2) - (1 if digit % 2 == 0 else 0))

    # print(digit, ref)
    total += calculate(left, 1) % (10**9 + 7)
print(total % (10**9 + 7))
