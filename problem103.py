"""
20 31 38 39 40 42 45

real    0m16.087s
user    0m16.086s
sys 0m0.008s


"""
from itertools import combinations
pattern={}
for i in range(1,5):
    pattern[i]=set()
    for vector in map(lambda x:"+".join(x),combinations("abcdefg",i)):
        pattern[i].add(vector)
def check(l):
    ref = {}
    ref[1] = set()
    for i in l:
        ref[1].add(int(i))
    temp = "abcdefg"
    for i in pattern:
        if i==1:
            continue
        ref[i] = set()
        for patt in pattern[i]:
            for j in range(len(temp)):
                patt=patt.replace(temp[j],l[j])
            try:
                t = eval(patt)
            except Exception as e:
                print(e,patt)
                raise e
            if t not in ref[i]:
                ref[i].add(t)
            else:
                return False
        if i-1!=0:
            # checking second condition
            if min(ref[i])<max(ref[i-1]):
                return False
            # checking first condition
            for j in range(1,i):
                if not ref[i].isdisjoint(ref[j]):
                    return False
    return True
for a in range(20,117):
    for b in range(1+a,117-a):
        for c in range(b+1,a+b):
            for d in range(c+1,a+b):
                for e in range(d+1,a+b):
                    for f in range(e+1,a+b):
                        for g in range(f+1,a+b):
                            if check([str(a),str(b),str(c),str(d),str(e),str(f),str(g)]):
                                print(a,b,c,d,e,f,g)
                                exit()