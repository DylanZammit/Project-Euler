from itertools import combinations

squares=[[[0,1]], [[0,4]], [[0,9], [0,6]], [[1,6], [1,9]],[[2,5]],[[3, 6], [3, 9]], [[4,6],[4,9]], [[9,4],[6,4]],[[8,1]]]

digits = list(range(10))
count = 0

for comb1 in combinations(digits, 6):
    for comb2 in combinations(digits, 6):
        for square in squares:
            found = False
            for pair in square:
                if pair[0] in comb1 and pair[1] in comb2 or pair[0] in comb2 and pair[1] in comb1:
                    found = True
            if not found: break
        if found: count+=1

print(count//2)