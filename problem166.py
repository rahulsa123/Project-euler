def backTracking(soduko):
    x , y = -1 ,-1
    for i in range(4):
        if soduko[i].count(-1)>0:
            x,y = i,soduko[i].index(-1)
            break
    if x==-1 and y == -1:
        return True

    for ele in range(10):
         safe = True
         for index in range(4):
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

