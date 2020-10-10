seqs = [[],[],[],[],[],[]]

def store_vals(arr, form):

	out = 1
	n=1
	while out <= 9999:
		if out >= 1000:
			arr.append(str(out))

		n+=1
		out = form(n)
		
store_vals(seqs[0], lambda n: n*(n+1)//2)
store_vals(seqs[1], lambda n: n**2)
store_vals(seqs[2], lambda n: n*(3*n-1)//2)
store_vals(seqs[3], lambda n: n*(2*n-1))
store_vals(seqs[4], lambda n: n*(5*n-3)//2)
store_vals(seqs[5], lambda n: n*(3*n-2))

def check_cyclic(arr):
    	
	first = 5
	# for j in range(1, len(arr)):
    # 	if first == arr[j]//100:
    # 		i=j

# new = seqs[n]

# for n in len(range(seqs, -1, -1)):
    	
# 	for x in new:
# 		p = n-1 if n > 0 else 0
# 		for y in seqs[p]:
# 			if y[:2] == x[2:]:
#     			new.append(y)
