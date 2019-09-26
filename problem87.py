# p**4 upto 84
# p**3 upto 368
# p**3 upto 7071

# prime calcultion
test_prime = [True]*8000

prime = []
p = 2
while p*p <= len(test_prime):
    if test_prime[p]:
        prime.append(p)
        for i in range(p*p, len(test_prime), p):
            test_prime[i] = False
    p += 1
for i in range(p, len(test_prime)):
    if test_prime[i]:
        prime.append(i)
# end
# print(prime)
p_4 = []
p_2 = []
p_3 = []

for i in prime:
    if i < 84+10:
        p_4.append(i**4)
    if i < 368+10:
        p_3.append(i**3)
    if i < 7071+10:
        p_2.append(i**2)
    else:
        break
counter = set()
for p4 in p_4:
    for p3 in p_3:
        if p3 + p4 > 50000000:
            break
        for p2 in p_2:
            if p4+p3+p2 < 50000000:
                counter.add(p2+p3+p4)
            else:
                break
print(len(counter))
