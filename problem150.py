print("take almost 2m11s")
l=[]
ref = []
t = 0
temp = 2**20
for k in range(1,500501):
    t = (615949*t+797807)%temp
    ref.append(t-(temp//2))
index = 0
num_element = 1
for row in range(1000):
    l.append(list(ref[index:index+num_element]))
    index+=num_element
    num_element+=1
for row in range(len(l)):
    # traverse backward of each col
    l[row][-1]= [l[row][-1],l[row][-1]]
    for each_ele in range(len(l[row])-2,-1,-1):
        l[row][each_ele]=[l[row][each_ele],l[row][each_ele]+l[row][each_ele+1][1]]
#exit()
minimum = l[0][0][-1]
for each_row in range(1,len(l)):
    for each_col in range(len(l[each_row])):
        remain_col = each_col+1
        total = l[each_row][each_col][0]
        minimum = min(minimum,total)
        for remain_row in range(each_row+1,len(l)):
            total+=(l[remain_row][each_col][1]-l[remain_row][remain_col][1]+l[remain_row][remain_col][0])
            remain_col+=1
            minimum = min(minimum,total)

print(minimum)
