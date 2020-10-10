from math import log10
log_2 = log10(2)

def first(n):
    d=1+int(n*log_2)
    return int(10**(n*log_2-d+3))

n=90
limit=678910
count=1
while count < limit:

    if first(n+196) == 123:
        n+=196
        count+=1
    else:
        if first(n+289) == 123:
            n+=289
            count+=1
        else:      
            n+=485
            count+=1  

print(n)