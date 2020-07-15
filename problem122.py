number = {x:[0,set()] for x in range(1,201)}

number[1][0]=0
number[1][1].add(1)
l=[0,0]
total = 0
for i in range(2,201):
 # getting previous value 
    ref_val = number[i-1][0] + 1
    ref_set = set(number[i-1][1])
    ref_set.add(i-1)
    # loop from i/2 to i-1 
    for j in range(i//2, i):
        # checking middle condition 
        if j+j == i and ref_val >= number[j][0]+1:
            ref_val = number[j][0]+1
            ref_set = set(number[j][1])
            ref_set.add(j)
        else:
            # first check number[j][0]+1 value is greater
            if number[j][0]+1>ref_val:
                continue 
            # checking if they equal then just update the set 
            if False and number[j][0]+1 == ref_val and i-j in number[j][1]:
                ref_set.update(number[j][1])
                ref_set.add(j)
            elif number[j][0]+1<ref_val and i-j in number[j][1]:
                ref_val = number[j][0]+1
                ref_set = set(number[j][1])
                ref_set.add(j)
        if i==71:
            print(i,j,ref_set)
            input()
    number[i][0] = ref_val
    number[i][1] = ref_set
    total+=ref_val
    l.append(ref_val)
import pprint
#pprint.PrettyPrinter(indent=0).pprint(number)
#for i in number:
#    print(i, number[i])

#print(total)
print(total)


