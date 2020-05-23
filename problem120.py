total = 0
for l in range(3, 1000+1):
    s = 0
    for n in range(1, 2*l+1):
        s = max(((pow(l-1,n,l**2)+pow(l+1,n,l**2))%l**2),s)
    total += s

print(total)
