"""
13459471903176422

real    9m8.927s
user    9m8.836s
sys 0m0.032s

"""

maxPower = 16
limit = 10**maxPower
result = 0


def solution(currDigit, currTotal, power, ref):
    # check currTotal+1 or -1 possible with ref
    global result
    temp = "".join(sorted(ref))

    if temp == "".join(sorted(str(currTotal + 1))):
        result += currTotal + 1
        # print(currTotal + 1, ref)
        return
    if temp == "".join(sorted(str(currTotal - 1))):
        result += currTotal - 1
        # print(currTotal - 1, ref)
        return
    if currTotal > limit or len(ref) >= maxPower or currDigit > 9:
        return

    # chossing digiit with some power
    for i in range(currDigit, 10):
        total = currTotal
        temp = ref[:]
        if power == 0:
            for k in range(2, maxPower + 1):
                total = currTotal
                temp = ref[:]
                if total + i**k >= limit:
                    break
                while(total + i**k < limit and len(temp) < maxPower):
                    total += i**k
                    temp += str(i)
                    solution(i + 1, total, k, temp)
        else:
            while(total + i**power < limit and len(temp) < maxPower):
                total += i**power
                temp += str(i)
                solution(i + 1, total, power, temp)


solution(currDigit=0, currTotal=0, power=0, ref="")
print(result)
