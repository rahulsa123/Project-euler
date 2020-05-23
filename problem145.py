"""
there is no 9 digit number exist for condition

"""
# how many digit numbers
ref = set("02468")
f = lambda x:set(str(x+int(str(x)[::-1]))).isdisjoint(ref)
count = 0
for digit_len in range(2,9):
    for first_digit in range(1,10):
        def get_numbers(first_digit, digit_len, num):
            global count   
            if digit_len == 1:
                for i in range(first_digit-1,0,-2):
                    if f(num*10+i):
                        count+=1

            else:
                for i in range(0,10):
                    get_numbers(first_digit,digit_len-1,num*10+i)

        get_numbers(first_digit, digit_len-1,first_digit)
print(2*count)