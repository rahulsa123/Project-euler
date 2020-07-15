count=0
for i in range(1000,9999):
     s=str(i)
     for j in set(s):
     #   if(i==3333):
       #     print(s.count("3"))
        if(s.count(j)>2):
            print(i)
            break
     else:
            count+=1
            
print(count)
