tri=[]
squ=[]
pe=[]
hexa=[]
hep=[]
octa=[]
for i in range(19,141):
    sq = i*i
    trii= (sq+i)/2
    ref=sq-trii
    if(trii>999 and trii<10000):
        tri.append(trii)
    if(sq>999 and sq<10000):
        squ.append(sq)
    for index ,item in enumerate(['pe','hexa','hep','octa']):
        temp= sq+(index+1)*ref
        if(temp>999 and temp<10000):
            eval(item+".append("+str(temp)+")")
#print(tri)
#print(squ)
#print(pe)

for o in octa:
    ref = [tri,squ,pe,hexa,hep]
    found=[]
    first_two_digit_1=o//100
    last_two_digit_1=o%100
   # print(o)
    for i in range(0,5):
        for j in range(len(ref[i])):
            first_two_digit_2=ref[i][j]//100
            last_two_digit_2=ref[i][j]%100
            if(first_two_digit_2>last_two_digit_1):
                break
            if(first_two_digit_2==last_two_digit_1):
               # print(" ",ref[i][j],i)
                for i1 in range(0,5):
                    if i1==i:
                        continue
                    for j1 in range(len(ref[i1])):
                        first_two_digit_3=ref[i1][j1]//100
                        last_two_digit_3=ref[i1][j1]%100
                        if(first_two_digit_3>last_two_digit_2):
                            break
                        if(first_two_digit_3==last_two_digit_2):
                          #  print("  ",ref[i1][j1])
                            for i2 in range(0,5):
                                if i2==i or i1==i2:
                                    continue
                                for j2 in range(len(ref[i2])):
                                    first_two_digit_4=ref[i2][j2]//100
                                    last_two_digit_4=ref[i2][j2]%100
                                    if(first_two_digit_4>last_two_digit_3):
                                        break
                                    if(first_two_digit_4==last_two_digit_3):
                             #       print("   ",ref[i2][j2])
                                        for i3 in range(0,5):
                                            if i3==i or i3==i2 or i3==i1:
                                                continue
                                            for j3 in range(len(ref[i3])):
                                                first_two_digit_5=ref[i3][j3]//100
                                                last_two_digit_5=ref[i3][j3]%100
                                                if(first_two_digit_5>last_two_digit_4):
                                                    break
                                                if(first_two_digit_5==last_two_digit_4):
                                                    for i4 in range(0,5):
                                                        if i4==i or i4==i1 or i4==i2 or i4==i3:
                                                            continue
                                                        for j4 in range(len(ref[i4])):
                                                            first_two_digit_6=ref[i4][j4]//100
                                                            last_two_digit_6=ref[i4][j4]%100
                                                            if(first_two_digit_6>last_two_digit_5):
                                                                break
                                                            if(first_two_digit_6==last_two_digit_5 and last_two_digit_6 == first_two_digit_1):
                                                                print(o,ref[i][j],i,ref[i1][j1],i1,ref[i2][j2],i2,ref[i3][j3],i3,ref[i4][j4],i4)
