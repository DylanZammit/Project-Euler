import time
start_time = time.time()

M=10**6

out = 0
B = 0
k=1

while B >= 0:
    out+=B
    B = (M+4*k**2)//(4*k)-(2*k+1)+1
    k+=1

print(out, float(time.time()-start_time), 'secs')