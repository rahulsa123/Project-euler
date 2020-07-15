n, m = 3, 4
ref = [[0]*n for _ in range(m)]

total = 0

result = [[-1]*n for _ in range(m)]


def calculate(ref, i_start, j_start):
    if all((0 not in x for x in ref)):
        return 1
    temp = 0
    global result
    for i in range(i_start, m):
        for j in range(j_start, n):

            if ref[i][j] == 0:
                if result[i][j]!=-1:
                    print("hitt")
                    return result[i][j]
                # means blank
                # filled indicate block is filled or not
                filled = False
                # now check each pattern of row size of 1 and colunm size 3
                if j < n-2 and ref[i][j+1] == ref[i][j+2] == 0:
                    filled = True
                    # set as filled
                    ref[i][j] = ref[i][j+1] = ref[i][j+2] = 6
                    i_ref, j_ref = i, j
                    # there is one left block avaliable
                    if j+3 < n:
                        i_ref,j_ref = i_ref,j_ref+3
                    else:
                        i_ref,j_ref = i_ref+1,j_ref
                    temp += calculate(ref, i,0)
                    # unset filled for furthur calculation
                    ref[i][j] = ref[i][j+1] = ref[i][j+2] = 0
                # now check each pattern of row size of 2 and colunm size 2
                if j < n-1 and i < m-1:
                    if ref[i][j+1] == ref[i+1][j] == 0:
                        filled = True
                        # set as filled
                        ref[i][j] = ref[i][j+1] = ref[i+1][j] = 1
                        # there is one left block avaliable
                        i_ref, j_ref = i, j
                        if j+2 < n:
                            i_ref,j_ref = i_ref,j_ref+2
                        else:
                            i_ref,j_ref = i_ref+1,j_ref+1
                        temp += calculate(ref, i,0)
                        # unset filled for furthur calculation
                        ref[i][j] = ref[i][j+1] = ref[i+1][j] = 0
                    if ref[i][j+1] == ref[i+1][j+1] == 0:
                        filled = True
                        # set as filled
                        ref[i][j] = ref[i][j+1] = ref[i+1][j+1] = 2
                        i_ref, j_ref = i, j
                        if j+2 < n:
                            i_ref,j_ref = i_ref,j_ref+2
                        else:
                            i_ref,j_ref = i_ref+1,j_ref
                        temp += calculate(ref, i,0)
                        # unset filled for furthur calculation
                        ref[i][j] = ref[i][j+1] = ref[i+1][j+1] = 0
                    if ref[i+1][j+1] == ref[i+1][j] == 0:
                        filled = True
                        # set as filled
                        ref[i][j] = ref[i+1][j+1] = ref[i+1][j] = 3
                        i_ref, j_ref = i, j
                        i_ref,j_ref = i_ref,j_ref+1
                        
                        temp += calculate(ref, i,0)
                        # unset filled for furthur calculation
                        ref[i][j] = ref[i+1][j+1] = ref[i+1][j] = 0

                # special case forth one
                if i < m-1 and j > 0 and ref[i+1][j] == ref[i+1][j-1] == 0:
                    filled = True
                    # set as filled
                    ref[i][j] = ref[i+1][j] = ref[i+1][j-1] = 4
                    i_ref, j_ref = i, j
                    if j+2 < n:
                        i_ref,j_ref = i_ref,j_ref+2
                    else:
                        i_ref,j_ref = i_ref+1,0
                    temp += calculate(ref, i,0)
                    # unset filled for furthur calculation
                    ref[i][j] = ref[i+1][j] = ref[i+1][j-1] = 0
                # now check each pattern of row size of 3 and colunm size 1
                if i < m-2 and ref[i+1][j] == ref[i+2][j] == 0:
                    filled = True
                    # set as filled
                    ref[i][j] = ref[i+1][j] = ref[i+2][j] = 5
                    i_ref, j_ref = i, j
                    if j+1 < n:
                        i_ref,j_ref = i_ref,j_ref+2
                    else:
                        i_ref,j_ref = i_ref+1,j_ref+1
                    temp += calculate(ref, i,0)
                    # unset filled for furthur calculation
                    ref[i][j] = ref[i+1][j] = ref[i+2][j] = 0
                result[i][j] = temp
                return temp
    return temp

print(calculate(ref, i_start=0, j_start=0))
print(total)
