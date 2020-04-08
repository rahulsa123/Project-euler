from primeupto import prime
max_limit = 10**9
p = prime(10**8)
total=0
def checkPrime(n):
	ref = n**0.5
	for i in p:
		if i>ref:
			return True
		if n%i==0:
			return False
	return True
for i in [1]+p:
    i*=10
    ref_true = [i**2+x for x in [1,3,7,9,13,27]]
	#ref_false = [i**2+x for x in [5,11,15,17,19,21,23,25]]
	#print(ref_true,ref_false)
    if all((checkPrime(x) for x in ref_true)):
        print(i)
        total+=i
print("t",total)
