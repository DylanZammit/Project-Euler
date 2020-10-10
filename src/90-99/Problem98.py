from math import log10
import collections
import numpy as np
import pickle

def are_words_anagram(a, b):
    a_letters = [x for x in a]
    b_letters = [x for x in b]
    return collections.Counter(a_letters) == collections.Counter(b_letters)

def are_nums_anagram(a, b):
    a_digits = [int(x) for x in str(a)]
    b_digits = [int(x) for x in str(b)]
    return collections.Counter(a_digits) == collections.Counter(b_digits)

def get_corresponding_anagram(anagrams, num):

    code = {}

    word_1 = anagrams[0]
    word_2 = anagrams[1]

    num = [int(x) for x in str(num)]

    out = []

    for i in range(len(word_1)):
        if num[i] in code:
            if word_1[i] != code[num[i]]:
                return -1
        else:
            code[num[i]] = word_1[i]

    for i in range(len(word_1)):
        a = word_1.index(word_2[i])
        word_1=word_1[:a]+'.'+word_1[a+1:]
        out.append(num[a])

    return int(''.join(map(str,out)))

words = []
with open('../p098_words.txt', 'r') as openfileobject:
    for line in openfileobject:
        words.append([x for x in line.split('","')])
words = [item for sublist in words for item in sublist]
words[0] = words[0][1:]
words[-1] = words[-1][:-1]

words_by_length = {}
for word in words:
    size = len(word)
    if str(size) in words_by_length:
        words_by_length[str(size)].append(word)
    else:
        words_by_length[str(size)] = [word]

squares = {}

n = 1
x = 1
z = 1
while x<=14:

    if str(x) in squares:
        squares[str(x)].append(z)
    else:
        squares[str(x)] = [z]

    n+=1
    z = n**2
    x = int(log10(z))+1

# filename = 'squares.pk'

# with open(filename, 'wb') as fi:
#     # dump your data into the file
#     pickle.dump(squares, fi)

# with open(filename, 'rb') as fi:
#     squares = pickle.load(fi)

word_anagrams = {}

maximum = 0

for word_length in words_by_length:
    word_arr = words_by_length[word_length]
    z=len(word_arr)

    list_anagrams = []
    
    for i in range(z):
        for j in range(i+1, z):
            if are_words_anagram(word_arr[i], word_arr[j]):
                list_anagrams.append([word_arr[i], word_arr[j]])
    
    for anagrams in list_anagrams:
        square = squares[word_length]
        i=0
        while i < len(square):
            num_anag = get_corresponding_anagram(anagrams, square[i])
            if num_anag in square and max(num_anag, square[i]) > maximum:
                maximum = max(num_anag, square[i])
                print(num_anag, square[i], anagrams)
            i+=1
print(maximum)

        
