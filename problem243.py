"""
892371480

real    0m8.656s
user    0m9.077s
sys 0m0.616s

here get_totient(i)*94744<15499*(i-1)
here i genrate number is more complex so totient value is very less compare to (i-1)
some facts i used
(2*4*6*10*12*16*18*22*28)/(2*3*5*7*11*13*17*19*23*29-1) ==> 0.156 
so maximum limit to genrate number is 2*3*5*7*11*13*17*19*23*29==6469693230
"""

from prime import get_number
def get_totient(n):
    for i in [2,3,5,7,11,13,17,19,23]:
        if n%i==0:
            n*=(i-1)
            n//=i
    return n

for i in get_number([2,3,5,7,11,13,17,19,23],6469693230):
    if get_totient(i)*94744<15499*(i-1):
        print(i)
        exit()