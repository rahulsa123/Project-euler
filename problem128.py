
from prime import is_prime
l1 = 2
l2 = 8
l3 = 20
l2_size = 2 # 6*l2_size 
corner_gape_l2 = 1
count = 2 # first 1 second 2
current_ans = 2

while(True):
	start_point = l2
	end_point = l2+6*l2_size-1
	start_ele_pd = 0
	end_ele_pd = 0
	if  is_prime(abs(6*l2_size-1)):
		start_ele_pd+=1
		end_ele_pd+=1
	# for start
	start_ele_pd+= is_prime(abs(l2-l3)) 
	start_ele_pd+=is_prime(abs(l2-(l3+1))) 
	start_ele_pd+=is_prime(abs(l2-(l3+6*(l2_size+1)-1))) 
	start_ele_pd+=is_prime(abs(l2-l1))
			
	# end
	end_ele_pd+= is_prime(abs(end_point-l1))  
	end_ele_pd+= is_prime(abs(end_point-(l1+6*(l2_size-1)-1))) 
	end_ele_pd+= is_prime(abs(end_point-(l3+6*(l2_size+1)-1))) 
	end_ele_pd+= is_prime(abs(end_point-(l3+6*(l2_size+1)-2))) 
	# print("pd",start_ele_pd)
	#print(start_point,start_ele_pd,abs(l2-l3),abs(l2-(l3+1)),abs(l2-(l3+6*(l2_size+1)-1)),abs(l2-l1))
	if start_ele_pd==3:
		count+=1
		current_ans = start_point
	if end_ele_pd ==3:
		count+=1
		current_ans = end_point
	if count == 2000:
		print(current_ans)
		break	
	l1 = l2
	l2 = l3
	l3 = l3+6*(l2_size+1)

	l2_size += 1 # 6*l2_size
"""
14516824220

real	0m3.088s
user	0m3.046s
sys	0m0.016s


"""