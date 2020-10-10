seqs = [[],[],[],[],[],[]]

def store_vals(arr, form):

	out = 1
	n=1
	while out <= 9999:
		if out >= 1000:
			arr.append(out)

		n+=1
		out = form(n)
		
store_vals(seqs[0], lambda n: n*(n+1)//2)
store_vals(seqs[1], lambda n: n**2)
store_vals(seqs[2], lambda n: n*(3*n-1)//2)
store_vals(seqs[3], lambda n: n*(2*n-1))
store_vals(seqs[4], lambda n: n*(5*n-3)//2)
store_vals(seqs[5], lambda n: n*(3*n-2))

def get_ans():
    for num in seqs[0]:
        out, flag = rec([1, 2, 3, 4, 5], num, num, [num])
        if flag: return out
    

def rec(indices, prev, first, sequence):

    if len(indices) == 0:
        if prev%100==first//100:
            return sequence, True
        return -1, False

    for i in indices:
        for num in seqs[i]:
            if prev%100==num//100:
                new_ind = indices.copy()
                new_ind.remove(i)

                new_seq = sequence.copy()
                new_seq.append(num)
                boq, flag = rec(new_ind, num, first, new_seq)
                if flag: return boq, True
    return -1, False
    

out = get_ans()
print(out)
print(sum(out))