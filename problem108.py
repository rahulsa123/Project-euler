step  = 0
n=2
max = 1
while(n<60):
    step = 0
    for x in range(n+1,2*n+1):
        if((n*x)%(x-n) ==0):
            step+=1
           # print(" n ",n,"x", x, "y" , (n*x)//(x-n))
    if(max<step):
       # print(n, step)
        max = step
    print("n " , n,"total",step) 
    if(max>1000):
        break
    n+=1
print(n,max)

