import numpy as np

def word_to_num(word):
    return sum([ord(c)-64 for c in word])

def is_triangular(k):
    n = 0.5 + np.sqrt(0.25+2*k)
    return n==int(n)

file = open('../Problem42.txt', 'r') 
words = file.read().split("\",\"")
words[0]=words[0][1]
words[-1]=words[-1][0]

out = 0

for word in words:
    if(is_triangular(word_to_num(word))):
        out +=1

    
print(out)