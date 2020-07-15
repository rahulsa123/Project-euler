first = 1504170715041707
base = 4503599627370517
minimum = first
total = minimum
i = 2
pre = 1
while(True):
    if minimum==1:
        break
    if minimum > divmod(first*i, base)[1]:
        minimum = divmod(first*i, base)[1]
        total+=minimum
        i, pre = 2*i-pre, i
        print(minimum,pre)
        continue
    i+=1
print(total)
