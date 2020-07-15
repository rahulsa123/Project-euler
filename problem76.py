maximum=99
counter=0
def getnu(n,su):
    global counter
    if(su==maximum):
      #  print(1)
        counter+=1
        return
    if(su>maximum-1):
        return
    if(n==1):
        return
    for i in range(0,maximum+1-su,n):
     #   print(" "*(maximum-n),n,i+su)
        getnu(n-1,su+i)
pre=1
for i in range(2,101):
    counter=pre
    maximum=i
    print(getnu(i-1,0),i,counter)
    pre=counter
