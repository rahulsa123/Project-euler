import math as m
min=8000000
for i in range(2,30000):
    for j in range(2,30000):
        if(min>m.fabs(8000000-(i*(i+1)*j*(j+1)))):
            min = m.fabs(8000000-(i*(i+1)*j*(j+1)))
            print(i,j,min)

