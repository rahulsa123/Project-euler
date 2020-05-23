"""
real    0m0.080s
user    0m0.048s
sys 0m0.008s




    blue    red     total
1   1       1       2
2   1       2       3
3   1       3       4
4   1       4       5
5   1       5       6
6   1       6       7
7   1       7       8
8   1       8       9
9   1       9       10
10  1       10      11
11  1       11      12
12  1       12      13
13  1       13      14
14  1       14      15
15  1       15      16

winning combination

blue 15
zero red    1

blue 14           (all combination of red value where r=1 ) and sum
1 red       120  


blue 13     6580    (all combination of red value where r=2 multiplication of each group) then sum
2 red                all values       

blue 12     218400
3 red

blue 11     4899622
4 red

blue 10     78558480
5 red

blue 9      928095740
6 red

blue 8      8207628000
7 red

now total_match/winning_combination  = factorial(16)/sum_of_above_values
"""
import itertools
import functools 
import math
total = 1 # base case where all 15 balls are blue
for i in range(2,8):
    total+=sum(functools.reduce(lambda x,y:x*y, x) for x in itertools.combinations(range(1,16),i))
print(int(math.factorial(16)/total))
