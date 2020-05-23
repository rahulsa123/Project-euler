"""
14234

real    0m3.787s
user    0m3.801s
sys 0m0.004s

(a,b)
        
        l1
        
            (c,d)
        
        l2
    
(0,0)
using  line equation 
m1((0,0),(c,d)) == c/d
m2((a,b),(c,d)) == (a-c)/(b-d)
                m1-m2
tan(angle) = -----------
                1+m1*m2
                cb-cd-ad-cd
tan(angle) = -----------------
                db-d**2+ac-c**2
for angle == 90 
    
    db-d**2+ac-c**2 == 0

"""
limit = 50
# zero
total = limit**2
# edges
total += 2*limit**2

for C in range(1,limit+1):
    for D in range(1,limit+1):
        ref = D-1
        for A in range(C+1, min((D**2+C**2)//C+1,limit+1)):
            for B in range(ref, -1,-1):
                if D*B-D**2+C*A-C**2==0:
                    total+=1
                    ref = B
        ref = C-1
        for A in range(ref, -1,-1):
            for B in range(D+1, min((D**2+C**2)//D+1,limit+1)):
                if D*B-D**2+C*A-C**2==0:
                    total+=1
                    ref = C
print(total)