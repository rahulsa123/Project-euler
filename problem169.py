"""
178653872807

real	0m0.048s
user	0m0.044s
sys	0m0.005s


"""



from collections import defaultdict
import math as m

"""

cache {
	curr_power : {
			n: number of ways to make using 2th power from 0 to curr_power
			}
}
"""

limit = 10**25
power = int(m.log2(limit))
cache = {x:defaultdict(int) for x in range(power+1)}
cache[0][1] = 1
cache[0][2] = 1
cache[1][2] = 2

def calculate(n,power):
	# print(n,power)
	ref = 2**power
	if n<0 or n>2*(2*ref-1) or power<0:
		return 0
	if n==0:
		return 1
	if cache[power][n]!=0:
		return cache[power][n]
	
	
	result = 0
	if n>=2*ref:
		result += calculate(n-2*ref,power-1)
	if n>=ref:
		result+=calculate(n-ref,power-1)
	if power>0:
		result+=calculate(n,power-1)
	cache[power][n] = result
	return result


print(calculate(limit,power))
