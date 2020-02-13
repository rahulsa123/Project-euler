import itertools 
l = list(itertools.combinations("0123456789",6))
s = [] 
for i in range(len(l)-1):
    ref1 = l[i]
    if "6" in ref1 and "9" not in ref1:
        ref1=ref1+ ("9",)
    elif "9" in ref1 and "6" not in ref1:
        ref1 = ref1+("6",)
    for j in range(i+1, len(l)):
        ref2 = l[j]
        if "6" in ref2 and "9" not in ref2:
            ref2 = ref2+("9",)
        elif "9" in ref2 and "6" not in ref2:
            ref2 = ref2+("6",)
        for k in ["01", "04", "09", "16", "25", "36", "49", "64","81"]:
            if not((k[0] in ref1 and k[1] in ref2) or ((k[1] in ref1 and k[0] in ref2))):
                break
        else:
            s.append((l[i],l[j]))
print(len(s))

