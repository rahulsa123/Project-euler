start=21780
found=19602
while(start-start/100!=found):
    start+=1
   # print(start)
    left,right=True,True
    s=str(start)
    for i in range(len(s)-1):
        if(s[i]>s[i+1]):
                left=False
                break
    for i in range(len(s)-1):
        if(s[i]<s[i+1]):
                right=False
                break
    if(not left and not right):
       # print(start)
        found+=1
    #else:
     #   print(start)
print(start,found)
