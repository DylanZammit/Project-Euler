import random
import numpy as np

def throw_dice():
    d1 = random.randint(1, 4)
    d2 = random.randint(1, 4)
    return d1, d2

community_cards = [0, 10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10]
chance_cards = [0, 10, 11, 24, 39, 5, -5, -5, -6, -3, -10, -10, -10, -10, -10, -10]
counts = [0]*40

def shuffle_community():
    random.shuffle(community_cards)

def shuffle_chance():
    random.shuffle(chance_cards)

def community(pos, count):
    cc = community_cards[count%16]
    if cc >= 0: return cc
    return pos

def chance(pos, count):
    ch = chance_cards[count%16]

    if ch >= 0: return ch
    if ch == -10: return pos
    if ch == -3: return pos-3
    if ch == -5: return 15 if pos == 7 else 25 if pos == 22 else 5 
    if ch == -6: return 12 if pos == 7 or pos == 36 else 28

M = 1000000
def check_square(pos, community_count, chance_count):
    if pos == 30:
        return 10, community_count, chance_count
    if pos in [7, 22, 36]:
        ch = chance(pos, chance_count)
        if ch == pos-3 and pos == 36:
            ch = community(ch, community_count)
            community_count+=1
        return ch, community_count, chance_count+1
    if pos in [2, 17, 33]:
        cc = community(pos, community_count)
        return cc, community_count+1, chance_count
    return pos, community_count, chance_count

def play_game():

    shuffle_community()
    shuffle_chance()

    double_count = 0
    pos = 0
    community_count = 0
    chance_count = 0

    for i in range(M):
        d1, d2 = throw_dice()
        if d1==d2:
            double_count+=1
        else:
            double_count=0
        if double_count == 3:
            pos = 10
            double_count = 0
        else:
            pos+=(d1+d2)
            pos%=40
            pos, community_count, chance_count = check_square(pos, community_count, chance_count)
        counts[pos]+=1
    return np.divide(counts, sum(counts))*100

out = play_game()

print(out)

a1=np.argmax(out)
out[a1]=0

a2=np.argmax(out)
out[a2]=0

a3=np.argmax(out)
out[a3]=0

print(a1, a2, a3)