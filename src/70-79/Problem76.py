import numpy as np

vals = {}

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
	return p_exact(100)-1
				
print(get_answer())



