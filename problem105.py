def combinationUtil(arr, n, r,  
                    index, data, i,l): 
    # Current combination is  
    # ready to be printed, 
    # print it 
    if(index == r): 
        l.append({data[x] for x in range(r)}) 
        return
  
    # When no more elements  
    # are there to put in data[] 
    if(i >= n): 
        return
  
    # current is included,  
    # put next at next 
    # location  
    data[index] = arr[i] 
    combinationUtil(arr, n, r,  
                    index + 1, data, i + 1,l) 
      
    # current is excluded,  
    # replace it with 
    # next (Note that i+1  
    # is passed, but index  
    # is not changed) 
    combinationUtil(arr, n, r, index,  
                    data, i + 1,l) 
  
  
# The main function that 
# prints all combinations 
# of size r in arr[] of  
# size n. This function  
# mainly uses combinationUtil() 
def printcombination(arr, n, r,l): 
  
    # A temporary array to 
    # store all combination 
    # one by one 
    data = list(range(r)) 
      
    # Print all combination  
    # using temporary  
    # array 'data[]' 
    combinationUtil(arr, n, r,  
                    0, data, 0,l) 
  
  
# Driver Code 
#arr = [157, 150, 164, 119, 79, 159, 161, 139, 158]
ref = [[81, 88, 75, 42, 87, 84, 86, 65],
[157, 150, 164, 119, 79, 159, 161, 139, 158],
[673, 465, 569, 603, 629, 592, 584, 300, 601, 599, 600],
[90, 85, 83, 84, 65, 87, 76, 46], 
[165, 168, 169, 190, 162, 85, 176, 167, 127], [224, 275, 278, 249, 277, 279, 289, 295, 139],
[354, 370, 362, 384, 359, 324, 360, 180, 350, 270], [599, 595, 557, 298, 448, 596, 577, 667, 597, 588, 602], 
[175, 199, 137, 88, 187, 173, 168, 171, 174], [93, 187, 196, 144, 185, 178, 186, 202, 182], 
[157, 155, 81, 158, 119, 176, 152, 167, 159], [184, 165, 159, 166, 163, 167, 174, 124, 83], 
[1211, 1212, 1287, 605, 1208, 1189, 1060, 1216, 1243, 1200, 908, 1210], [339, 299, 153, 305, 282, 304, 313, 306, 302, 228], 
[94, 104, 63, 112, 80, 84, 93, 96], [41, 88, 82, 85, 61, 74, 83, 81], [90, 67, 84, 83, 82, 97, 86, 41], 
[299, 303, 151, 301, 291, 302, 307, 377, 333, 280], [55, 40, 48, 44, 25, 42, 41], 
[1038, 1188, 1255, 1184, 594, 890, 1173, 1151, 1186, 1203, 1187, 1195], [76, 132, 133, 144, 135, 99, 128, 154], 
[77, 46, 108, 81, 85, 84, 93, 83], [624, 596, 391, 605, 529, 610, 607, 568, 604, 603, 453], 
[83, 167, 166, 189, 163, 174, 160, 165, 133], 
[308, 281, 389, 292, 346, 303, 302, 304, 300, 173], 
[593, 1151, 1187, 1184, 890, 1040, 1173, 1186, 1195, 1255, 1188, 1203], 
[68, 46, 64, 33, 60, 58, 65], [65, 43, 88, 87, 86, 99, 93, 90], [83, 78, 107, 48, 84, 87, 96, 85], 
[1188, 1173, 1256, 1038, 1187, 1151, 890, 1186, 1184, 1203, 594, 1195], [302, 324, 280, 296, 294, 160, 367, 298, 264, 299],
[521, 760, 682, 687, 646, 664, 342, 698, 692, 686, 672], 
[56, 95, 86, 97, 96, 89, 108, 120], [344, 356, 262, 343, 340, 382, 337, 175, 361, 330], 
[47, 44, 42, 27, 41, 40, 37], [139, 155, 161, 158, 118, 166, 154, 156, 78], 
[118, 157, 164, 158, 161, 79, 139, 150, 159], [299, 292, 371, 150, 300, 301, 281, 303, 306, 262], 
[85, 77, 86, 84, 44, 88, 91, 67], [88, 85, 84, 44, 65, 91, 76, 86], [138, 141, 127, 96, 136, 154, 135, 76], 
[292, 308, 302, 346, 300, 324, 304, 305, 238, 166], [354, 342, 341, 257, 348, 343, 345, 321, 170, 301], 
[84, 178, 168, 167, 131, 170, 193, 166, 162], [686, 701, 706, 673, 694, 687, 652, 343, 683, 606, 518], 
[295, 293, 301, 367, 296, 279, 297, 263, 323, 159], [1038, 1184, 593, 890, 1188, 1173, 1187, 1186, 1195, 1150, 1203, 1255],
[343, 364, 388, 402, 191, 383, 382, 385, 288, 374], [1187, 1036, 1183, 591, 1184, 1175, 888, 1197, 1182, 1219, 1115, 1167],
[151, 291, 307, 303, 345, 238, 299, 323, 301, 302], [140, 151, 143, 138, 99, 69, 131, 137], [29, 44, 42, 59, 41, 36, 40], 
[348, 329, 343, 344, 338, 315, 169, 359, 375, 271], [48, 39, 34, 37, 50, 40, 41],
[593, 445, 595, 558, 662, 602, 591, 297, 610, 580, 594], [686, 651, 681, 342, 541, 687, 691, 707, 604, 675, 699],
[180, 99, 189, 166, 194, 188, 144, 187, 199], [321, 349, 335, 343, 377, 176, 265, 356, 344, 332], 
[1151, 1255, 1195, 1173, 1184, 1186, 1188, 1187, 1203, 593, 1038, 891], [90, 88, 100, 83, 62, 113, 80, 89],
[308, 303, 238, 300, 151, 304, 324, 293, 346, 302], [59, 38, 50, 41, 42, 35, 40], 
[352, 366, 174, 355, 344, 265, 343, 310, 338, 331], [91, 89, 93, 90, 117, 85, 60, 106], 
[146, 186, 166, 175, 202, 92, 184, 183, 189], [82, 67, 96, 44, 80, 79, 88, 76], [54, 50, 58, 66, 31, 61, 64], 
[343, 266, 344, 172, 308, 336, 364, 350, 359, 333], [88, 49, 87, 82, 90, 98, 86, 115], [20, 47, 49, 51, 54, 48, 40],
[159, 79, 177, 158, 157, 152, 155, 167, 118], [1219, 1183, 1182, 1115, 1035, 1186, 591, 1197, 1167, 887, 1184, 1175],
[611, 518, 693, 343, 704, 667, 686, 682, 677, 687, 725], [607, 599, 634, 305, 677, 604, 603, 580, 452, 605, 591], 
[682, 686, 635, 675, 692, 730, 687, 342, 517, 658, 695], [662, 296, 573, 598, 592, 584, 553, 593, 595, 443, 591],
[180, 185, 186, 199, 187, 210, 93, 177, 149], [197, 136, 179, 185, 156, 182, 180, 178, 99],
[271, 298, 218, 279, 285, 282, 280, 238, 140], [1187, 1151, 890, 593, 1194, 1188, 1184, 1173, 1038, 1186, 1255, 1203],
[169, 161, 177, 192, 130, 165, 84, 167, 168], [50, 42, 43, 41, 66, 39, 36], 
[590, 669, 604, 579, 448, 599, 560, 299, 601, 597, 598], [174, 191, 206, 179, 184, 142, 177, 180, 90],
[298, 299, 297, 306, 164, 285, 374, 269, 329, 295], [181, 172, 162, 138, 170, 195, 86, 169, 168],
[1184, 1197, 591, 1182, 1186, 889, 1167, 1219, 1183, 1033, 1115, 1175],
[644, 695, 691, 679, 667, 687, 340, 681, 770, 686, 517], [606, 524, 592, 576, 628, 593, 591, 584, 296, 444, 595],
[94, 127, 154, 138, 135, 74, 136, 141], [179, 168, 172, 178, 177, 89, 198, 186, 137],
[302, 299, 291, 300, 298, 149, 260, 305, 280, 370], [678, 517, 670, 686, 682, 768, 687, 648, 342, 692, 702], 
[302, 290, 304, 376, 333, 303, 306, 298, 279, 153], [95, 102, 109, 54, 96, 75, 85, 97], 
[150, 154, 146, 78, 152, 151, 162, 173, 119], [150, 143, 157, 152, 184, 112, 154, 151, 132], [36, 41, 54, 40, 25, 44, 42],
[37, 48, 34, 59, 39, 41, 40], [681, 603, 638, 611, 584, 303, 454, 607, 606, 605, 596]]
total=0
for index,arr in enumerate(ref):
    found = True
    l=[]
    if len(arr)!= len(set(arr)):
        continue
    arr.sort()
    for r in range(2,len(arr)-1):
        n = len(arr) 
        printcombination(arr, n, r,l)
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if len(l[i].intersection(l[j]))==0 and len(l[j].intersection(l[i]))==0 and (sum(l[i])==sum(l[j]) or len(l[i])>len(l[j]) and sum(l[i])< sum(l[j]) or len(l[j])>len(l[i]) and sum(l[j])< sum(l[i])):
                #print(index,arr,l[i],l[j])
                found = False 
                break
        if not found:
            break
    if found:
        print(index,arr,sum(arr),total)
        total+=sum(arr)
print(total)

