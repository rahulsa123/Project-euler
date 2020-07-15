maximum = 0
for n in range(30517578125,1000**10):
    c=4
    radius = n/(2**0.5)
    #low = int(n/2 - radius-1)
    #high = int(n/2 +radius+1)
   # print(low,high)
    for x in range(1,n//2+1):
        """
        for y in range(low,high):
            if x**2+y**2 == n*(x+y):
                print(c,x,y)
                c+=1
        """
        
        ref =4*(x**2-n*x)
        if n**2 <ref:
            continue 
        d = (n**2-ref)**0.5
        if int(d)==d and n%2==d%2:
            y1 = (n+d)/2
            #y2 = (n-d)/2
            if x**2+y1**2 == n*(x+y1):
                #if x>0 and x<n/2 and y1>0:
                print(c,x,y1)
                c+=8
            if False and  x**2+y2**2 == n*(x+y2):
                #if x>0 and x<n/2 and y2>0:
                print(c,x,y2)
                #print(c,x,y2) 
                c+=1
    print(n,c)
    break
