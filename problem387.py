import collections

s = collections.deque()
max_limit = 10**(13)
strong = collections.deque()



def checkPrime(num):
    if num == 2:
        return True
    if (divmod(num, 2)[1] == 0) or num == 1:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if divmod(num, i)[1] == 0:
            return False
    return True


def calculate(num, ref):
    global s
    if num > max_limit:
        return

    if divmod(num, ref)[1] == 0:
        s.append(num)
        if checkPrime(num//ref):
            strong.append(num)
    else:
        return
    for i in range(0, 10):
        calculate(num * 10 + i, ref + i)


for digit in [1, 2, 4, 6, 8]:
    calculate(digit, digit)
# print(len(s))
total = 0

temp = [1, 3, 7, 9]
for i in strong:
    for ref in temp:
        if checkPrime(i * 10 + ref):
            total += i*10+ref
            # print(i*10+ref)
print(total)

