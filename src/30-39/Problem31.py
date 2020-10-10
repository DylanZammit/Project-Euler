
coins = [1, 2, 5, 10, 20, 50, 100, 200]

out = 0

accum = 0

for a in range(0, 200+1, 200):
    for b in range(a, 200+1, 100):
        for c in range(b, 200+1, 50):
            for d in range(c, 200+1, 20):
                for e in range(d, 200+1, 10):
                    for f in range(e, 200+1, 5):
                        for g in range(f, 200+1, 2):
                            out+=1
                                

print(out)