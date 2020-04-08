x = 3
f = lambda x : int(x)==x
while(True):
    # using x value to calculate y value
    for ref_y in range(int((x+2)**0.5+1),int((2*x-1)**0.5+1)):
         y = ref_y**2-x
         if y==0 or not f((x-y)**0.5):
             continue
         for ref_z in range(int((y+1)**0.5+1),int((2*y-1)**0.5+1)):
             z = ref_z**2-y
             if z!=0 and f((y-z)**0.5) and f((x-z)**0.5) and f((x+z)**0.5):
                 print(x,y,z)
    x+=1

