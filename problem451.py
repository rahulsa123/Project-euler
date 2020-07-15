limit = 100
ref = [1]*(limit+1)
squre_limit = int((limit+1)**0.5)
for i in range(2, limit-1):
    # i == 11
    temp = i**2-1 # 120
    # now all factor of temp
    try:
        for j in range(min(int(temp**0.5), limit-2), 0, -1):
            if temp % j == 0 and temp//j<limit+1 and temp//j-1!= i:
                ref[temp//j] = max(i, ref[temp//j])
    except Exception as e:
        print(temp, j, i)
        exit()

print([ref[x] for x in [6,10,15,14,21]])
