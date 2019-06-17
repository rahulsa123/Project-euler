"""
first how to genrate all fraction is order
       0/1                 1/1                   1/0  
                                            (lets take it 1/0 then just find middle one using addition of numerator with numerator and same with deno.)
       0/1    0+1/1+1=1/2      1/1    1+1/1+0 =2/1       0/1
       
       0/1   0+1/1+2=1/3   1/2    1+1/2+1=2/3   1/1  1+2/1+1=3/2  2/1     0/1

and so on just calculate using variable

"""


x1=2
x2=5
g1=3
g2=7
while(True):
    if(x2+g2>1000000):
        break
    x1+=g1
    x2+=g2
print(x1,x2)
