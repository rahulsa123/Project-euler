l=[[7, 53, 183, 439, 863, 497, 383, 563, 79, 973, 287, 63, 343, 169, 583], [627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913], [447, 283, 463, 29, 23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743], [217, 623, 3, 399, 853, 407, 103, 983, 89, 463, 290, 516, 212, 462, 350], [960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350], [870, 456, 192, 162, 593, 473, 915, 45, 989, 873, 823, 965, 425, 329, 803], [973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326], [322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601, 95, 973], [445, 721, 11, 525, 473, 65, 511, 164, 138, 672, 18, 428, 154, 448, 848], [414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198], [184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390], [821, 461, 843, 513, 17, 901, 711, 993, 293, 157, 274, 94, 192, 156, 574], [34, 124, 4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699], [815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107], [813, 883, 451, 509, 615, 77, 281, 613, 459, 205, 380, 274, 302, 35, 805]]
#print(l)
#exit()
x=[[7, 53, 183, 439, 863], [497, 383, 563, 79, 973], [287, 63, 343, 169, 583], [627, 343, 773, 959, 943], [767, 473, 103, 699, 303]] 
z = [[  7,  53, 183, 439, 863, 497, 383, 563],
       [627, 343, 773, 959, 943, 767, 473, 103],
       [447, 283, 463,  29,  23, 487, 463, 993],
       [217, 623,   3, 399, 853, 407, 103, 983],
       [960, 376, 682, 962, 300, 780, 486, 502],
       [870, 456, 192, 162, 593, 473, 915,  45],
       [973, 965, 905, 919, 133, 673, 665, 235],
       [322, 148, 972, 962, 286, 255, 941, 541]]
t = [[  7,  53, 183, 439, 863, 497, 383, 563,  79, 973],
       [627, 343, 773, 959, 943, 767, 473, 103, 699, 303],
       [447, 283, 463,  29,  23, 487, 463, 993, 119, 883],
       [217, 623,   3, 399, 853, 407, 103, 983,  89, 463],
       [960, 376, 682, 962, 300, 780, 486, 502, 912, 800],
       [870, 456, 192, 162, 593, 473, 915,  45, 989, 873],
       [973, 965, 905, 919, 133, 673, 665, 235, 509, 613],
       [322, 148, 972, 962, 286, 255, 941, 541, 265, 323],
       [445, 721,  11, 525, 473,  65, 511, 164, 138, 672],
       [414, 456, 310, 312, 798, 104, 566, 520, 302, 248]]
print(l)
import numpy as np 
a = np.array(l)
# make all element negative for maximum solution 
#print(l)
#exit()
ref2 = a.max()
a[:,:]*=-1
a[:,:]+=ref2
ROW, COLUMN = len(a),len(a)

# row minimmum subtraction 
for i in range(ROW):
    a[i]-=min(a[i])
#print(a)
# column minimum subtraction 
for i,data in enumerate(a.min(axis=0)):
    a[:,i]-=data 
#print(a)
#print(i)
def minimmum_cover(covered_data):
    # ROW covering first iff there one zero in row then put zero column in cover data  
    for i in range(ROW):
        r1 = np.where(a[i]==0)[0]
        ref = np.setdiff1d(r1, covered_data["COLUMN"])
        if len(ref)==1:
            covered_data["COLUMN"].append(ref[0])

    # COLUMN covering first iff there one zero in row then put zero column in cover data  
    for j in range(COLUMN):
        if j in covered_data["COLUMN"]:
            continue 
        r1 = np.where(a[:,j]==0)
        ref = np.setdiff1d(r1, covered_data["ROW"])
        if len(ref)==1:
            covered_data["ROW"].append(ref[0])
    # checking all zero covered or note 
    cover = True
    for i in range(ROW):
        if i in covered_data["ROW"]:
            continue 
        r1 = np.where(a[i]==0)[0]
        ref = np.setdiff1d(r1, covered_data["COLUMN"])
        if len(ref)>0:
            print("NOT cover", i, ref, covered_data)
            print(a)
            input()
            cover = False
            break 
    if not cover :
        minimmum_cover(covered_data)
#print(l)
while(True):
    print("array")
    print(a)
    covered_data = {"ROW":[], "COLUMN":[]}
    minimmum_cover(covered_data)
    print(covered_data)
    input()
    if len(covered_data["ROW"])+len(covered_data["COLUMN"])<ROW:
        # now find minimum from all the uncovered element 
        minimum_uncover = 99999999
        for i in range(ROW):
            if i not in covered_data["ROW"]:
                for j in range(COLUMN):
                    if j not in covered_data["COLUMN"]:
                        minimum_uncover = min(a[i][j], minimum_uncover)
        # subtract from all uncovered element and add who covered twice
        for i in range(ROW):
            for j in range(COLUMN):
                # check element covered twice 
                if i in covered_data["ROW"] and j in covered_data["COLUMN"]:
                    a[i][j]+=minimum_uncover
                elif i not in covered_data["ROW"] and j not in covered_data["COLUMN"]:
                    a[i][j]-=minimum_uncover 
    else:
        break

# all zero gives optimum result 
print("outter loop",a)
#input()
result = 0
s = ""
p = []
def get_result(row, col, temp, ref1):
    global result, s,p
    if row >-1:

        index = np.where(a[row]==0)[0]
        if row==13:
            print(index)
        for j in index:
            if col[j]!= 1:
                col[j]=1
                get_result(row-1, col, temp+l[row][j], ref1+str(row)+":"+str(j)+"-"+str(l[row][j])+"\n")
                col[j]=0
    if  result<temp:
        result = temp
        s = ref1    
        p = list(col)
get_result(ROW-1 ,[0]*COLUMN, 0,"")
print(result, s)
print(p)







