import re
import itertools as it
size=1000000
prime= [True]*(size+1)
p=2
l=[]
#print(" \n\n\n ")
while(p*p<=size):
    if(prime[p]==True):
       # if(p>999 and p<10000):
        l.append(str(p))
        for i in range(p+p,size+1,p):
            prime[i]=False
           # print(i,end=" ")
    p+=1
for i in range(p,size+1):
    if(prime[i]==True):
        # if(i>999):
        l.append(str(i))
#print(l[-10:])
gma=0
for i in l[l.index("56993"):]:
    s = str(i)
    ma=0
    if(s.find("0")!=-1):
        index = [x.start() for x in re.finditer('0', s)]
        for i in range(1,len(s)):
            for j in it.combinations(index,r=i):
                ref = s
                su=1
                fail=0
                mi = s
                for k in "123456789":
                    for m in j:
                        ref= ref[:m]+k+ref[m+1:]
 #                   print(ref,end=" ")
                    if(ref in l):
                        su+=1
                        mi=min(mi,ref)
                    else:
                        fail+=1
  #                      print("No")
                    if(su==8):
                        print(mi)
                        exit()
                    if(fail==3):
                        break
                ma=max(ma,su)
    if(s.find("1")!=-1):
        index = [x.start() for x in re.finditer('1', s)]
        for i in range(1,len(s)):
            for j in it.combinations(index,r=i):
                ref = s
                su=1
                fail=0
                mi = s
                for k in "023456789":
                    for m in j:
                        ref= ref[:m]+k+ref[m+1:]
   #                 print(ref,end=" ")
                    if(ref in l):
                        su+=1
                        mi=min(mi,ref)
                    else:
                        fail+=1
    #                    print("No")
                    if(su==8):
                        print(mi)
                        exit()
                    if(fail==3):
                        break
                ma=max(ma,su)
    if(s.find("2")!=-1):
        index = [x.start() for x in re.finditer('2', s)]
        for i in range(1,len(s)):
            for j in it.combinations(index,r=i):
                ref = s
                su=1
                fail=0
                mi = s
                for k in "103456789":
                    for m in j:
                        ref= ref[:m]+k+ref[m+1:]
     #               print(ref,end=" ")
                    if(ref in l):
                        su+=1
                        mi=min(mi,ref)
                    else:
                        fail+=1
      #                  print("No")
                    if(su==8):
                        print(mi)
                        exit()
                    if(fail==3):
                        break
                ma=max(ma,su)
    if(gma<ma):
        print(s,ma)
        gma=ma

