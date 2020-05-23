import prime
test1 = [1,3,7,9,13,27]
test2 = [21]
total=0
for i in range(10,150*10**6,10):
    squared = i**2
    if (squared % 3 != 1):
        continue
    ref = squared % 7
    if ( ref != 2 and ref != 3):
        continue
    if (squared % 13 == 0):
        continue
    if not any((prime.is_prime(squared+x) for x in test2)) and all((prime.is_prime(squared+x) for x in test1 )):
        #print(i)
        total+=i
print(total)
