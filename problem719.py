
def calculate(string,index,result):
    if index==len(string):
        if sum([int(x) for x in string.split("+")])==result:
            print(result,string)
            return True
        return False
    return calculate(string[:index]+"+"+string[index:],index+2,result) or \
        calculate(string,index+1,result)
total=0
for i in range(2,500+1):
    if i%9 == (i**2)%9 and calculate(str(i**2),1,i):
    	
    	total+=i**2
print(total)
