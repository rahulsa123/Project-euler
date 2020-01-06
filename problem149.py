
l=[0]
num = []
for k in range(1,56):
    ref = ((100003-200003*k+300007*k**3)%1000000)-500000
    l.append(ref)
for k in range(56,40000000+1):
    l.append((l[k-24]+l[k-55]+1000000)%1000000-500000)
index = 1
#print(l[:10])
for i in range(2000):
    ref = []
    for j in range(2000):
        ref.append(l[index])
        index+=1
    num.append(ref)
del l 
"""
with open('exam', 'wb') as f:
    import pickle 
    pickle.dump(num, f)
"""
#num = None
#with open('exam', 'rb') as f:
 #   import pickle 
#    num=pickle.load(f)
#print(num[0][:10])
#num = [[-2,5,3,2],[9,-6,5,1],[3,2,7,3],[-1,8,-4,8]]
total_maximum = 0
for select in range(2000):
    max_row,max_column, max_left_of_mid_diagonal, max_right_of_mid_diagonal = 0,0,0,0
    row, column, left_of_mid_diagonal, right_of_mid_diagonal = 0,0,0,0
    for move in range(2000):
        # row 
        row+=num[select][move]
        if row<0:
            row = 0
        max_row = max(max_row, row)
        # column 
        column+= num[move][select]
        if column<0:
            column=0
        max_column = max(max_column, column)
        # diagonal left of mid diagonal 
        # starting point num[select-0][0] then num[select-1][0+1]
        if select-move>-1:
            left_of_mid_diagonal+=num[select-move][move]
            left_of_mid_diagonal = 0 if left_of_mid_diagonal<0 else left_of_mid_diagonal
            max_left_of_mid_diagonal = max(max_left_of_mid_diagonal,left_of_mid_diagonal)
        #diagonal right of mid diagonal 
        # starting point num[1999][0] then num[1999-1][1]
        if select+move<2000:
            right_of_mid_diagonal+=num[1999-move][select+move]
            right_of_mid_diagonal = 0 if right_of_mid_diagonal<0 else right_of_mid_diagonal
            max_right_of_mid_diagonal = max(max_right_of_mid_diagonal, right_of_mid_diagonal)

        total_maximum = max(total_maximum,max_row, max_right_of_mid_diagonal, max_column, max_left_of_mid_diagonal)     
print(total_maximum)
