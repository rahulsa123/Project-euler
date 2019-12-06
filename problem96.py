import pprint
l = ['200080300', '060070084', '030500209', '000105408',
     '000000000', '402706000', '301007040', '720040060', '004010003']

def backTracking(soduko):
    x , y = -1 ,-1
    for i in range(9):
        if soduko[i].count(0)>0:
            x,y = i,soduko[i].index(0)
            break
    if x==-1 and y == -1:
        return True

    for ele in range(1,10):
         safe = True
         for index in range(9):
             if (soduko[x][index] == ele ) or (soduko[index][y]==ele):
                 safe = False
                 break
         if not safe:
             continue
         # for box
         i = x - x%3
         j = y - y%3
         for index_x in range(3):
             for index_y in range(3):
                 if (soduko[i+index_x][j+index_y]==ele):
                     safe = False
                     break
             if not safe:
                 break
         if not safe:
             continue 
         soduko[x][y]=ele 
         if backTracking(soduko):
             return True
         soduko[x][y] = 0
         
    return False    
    #if solved:
total = 0 
with open("/home/rahul/p096.txt", 'r') as f :
    for i in range(50):
        print(i)
        l = [next(f) for x in range(10)]
        l = l[1:]
        for i in range(len(l)):
            l[i] = l[i][:9]
        
        soduko = []
        for i in l:
            soduko.append([int(x) for x in i])
        backTracking(soduko)
        pprint.PrettyPrinter().pprint(soduko)
        total += soduko[0][0]*100 + soduko[0][1]*10+soduko[0][2]
        print(total)
print(total)

