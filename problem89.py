digit = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9:  "IX",
    5: "V",
    4: "IV",
    1: "I",
}
reverse = {
    "M": 1000,
    "CM":    900,
    "D":    500,
    "CD":    400,
    "C":    100,
    "XC":    90,
    "L":    50,
    "XL":    40,
    "X":    10,
    "IX":    9,
    "V":    5,
    "IV":    4,
    "I":    1
}
total = 0
l = []
for i in range(1000):
    l.append(input())
for ref in l:
    num = 0
    i=0
    while(i<len(ref)):
        if (ref[i]=="C") and (i+1<len(ref) and (ref[i+1] in ["D", "M"])):
            num+= reverse[ref[i]+ref[i+1]]
            i+=2
            continue
        if (ref[i]=="X") and (i+1<len(ref) and (ref[i+1] in ["L", "C"])):
            num+= reverse[ref[i]+ref[i+1]]
            i+=2
            continue
        if (ref[i]=="I") and (i+1<len(ref) and (ref[i+1] in ["V", "X"])):
            num+= reverse[ref[i]+ref[i+1]]
            i+=2
            continue
        num+=reverse[ref[i]]
        i+=1
#   print(ref, num)


    def num_to_roman(num):
        ref1 = ""
        for r in digit:
            while(num >= r):
                ref1 += digit[r]
                num -= r
            if num == 0:
                break
        return ref1

    s = num_to_roman(num)
#   print(s)
#    if len(ref)>len(s):
#       print(num,ref,s)
#      input()
    total+=len(ref)-len(s)
print(total)
