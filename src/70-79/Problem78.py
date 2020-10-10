import numpy as np
import time

start_time = time.time()

vals = {}

display_counter = False

def p_exact(n):
    
	if n == 0: return 1
	if n == 1: return 1
    	
	gk, k, out = 1, 1, 0

	while n-gk >= 0:
    		
		key = str(n-gk)

		if key in vals:
			term = vals[key]
		else:
			term = p_exact(n-gk)
			vals[key] = term

		out += int((-1)**(k-1))*term

		k = -k + 1 if k < 0 else -k
		
		gk = pentag(k)

	return out
    	
def pentag(k):
	return k*(3*k-1)/2		

def get_answer():
	k = 3
	
	while True:
		curr = p_exact(k)
		if curr%1000000==0:
			return k

		if k%5000==0 and display_counter:
			print(k)

		k+=1
				

elapsed_time = time.time() - start_time

print(get_answer(), elapsed_time)



