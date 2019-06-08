#takes >2min
import time
prime=[0]*100000000
p=2 
su =0
t=time.time()
while(p*p<100000000):
    if(prime[p]==1):
        for i in range(2,int((p-1)**0.5)+1):
            if((p-1)%i==0):
                if not(prime[(i+(p-1)//i)]==1):
                    break
        else:
            su+=p-1
           # print(p-1)
        for i in range(p+p,100000000,p):
            prime[i]=0
    p+=1
for j in range(p+1,100000000-2):
    if(prime[j+1]==1):
        for i in range(2,int((j)**0.5)+1):
            if((j)%i==0):
                if not(prime[(i+(j)//i)]==1):
                    break
        else:
            su+=j
           # print(j)
print(su,time.time()-t)
