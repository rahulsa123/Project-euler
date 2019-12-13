#[number, rad(number), prime or not ]
d = [[x,0,True] for x in range(0,100001)]
prime = []
d[1][1],d[1][2]=1,False
p = 2
while p<=100000:
    if d[p][2]:
        d[p][1]=p 
#        if p<389:
 #           prime.append(p)
        for i in range(p+p, 100001,p):
            d[i][2]= False
            if d[i][1]==0:
                d[i][1] = p 
            else:
                d[i][1]*=p  
    p+=1
#print(d[:11])
d.sort(key=lambda x : x[1])
#print(d[:1001])
#print(prime)
print(d[10000][0])
