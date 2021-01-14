"""
real    0m5.832s
user    0m5.777s
sys 0m0.008s



start from back

x

now seq is apply in reverse order

D=3*x
U=(3x-2)/4
d = (3x+1)/2

here end result must be in form of
x= end value we get after appling seq.

 (3^(length of sequence)*x + top)/ bottom

now here we need to calculate top and bottom

first reverse the seq. 
initial value

top = 0
bottom = 1

for each in reverse(seq)=>
    top*=3
    if i=="d":
        top+=bottom
        bottom*=2
    elif i=="U":
        top-=2*bottom
        bottom*=4

now just need to find x value (x>10**7)
"""
seq = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
# print(len(seq))
top = 0
bottom = 1
for i in seq[::-1]:
    top*=3
    if i=="d":
        top+=bottom
        bottom*=2
    elif i=="U":
        top-=2*bottom
        bottom*=4
# print(top, bottom)

xcons  = 3**30 
xcons_mod = xcons%bottom
top_mod = top%bottom

for i in range(10**7,10**9):
    ref = (xcons*i+top)%bottom
    if ref ==0 and (xcons*i+top)/bottom>10**15:
        print((xcons*i+top)/bottom,i)
        exit()