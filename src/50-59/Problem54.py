import numpy as np

hands = []

with open('../p054_poker.txt', 'r') as openfileobject:
    for line in openfileobject:
        hands.append([x for x in line.split()])

def split_hands(hand):
    suits=[]
    val=[]
    for card in hand:
        val.append(card[:-1])
        suits.append(card[-1])

    val = [10 if v=='T' else 11 if v=='J' else 12 if v=='Q' else 13 if v=='K' else 14 if v=='A' else int(v) for v in val]

    return suits,val

def royal(hand):
    
    suits,val = split_hands(hand)

    return 10 in val and 11 in val and 12 in val and 13 in val and 14 in val and len(set(suits))==1

def straight_flush(hand):

    suits,val = split_hands(hand)
        
    val = np.sort(val)
    return high_card(hand) if (len(set(val)) == 5 and val[-1]-val[0] == 4 and len(set(suits))==1) else 0

def four_kind(hand):

    suits,val = split_hands(hand)

    occs=[]
    out=[]

    for x in set(val):
        if(val.count(x)==4): return x

    return 0

def full_house(hand):
    
    suits,val = split_hands(hand)

    occs=[]

    out=0

    for x in set(val):
        occs.append(val.count(x))
        if(occs[-1]==3): out=x

    return out if 3 in occs and 2 in occs else 0

def flush(hand):
    
    suits,val = split_hands(hand)

    return high_card(hand) if len(set(suits))==1 else 0

def straight(hand):

    suits,val = split_hands(hand)
        
    val = np.sort(val)
    return high_card(hand) if len(set(val)) == 5 and val[-1]-val[0] == 4 else 0


def three_kind(hand):
    
    suits,val = split_hands(hand)

    for x in set(val):
        if val.count(x)==3:
            return x 

    return 0

def two_pairs(hand):
    
    suits,val = split_hands(hand)

    occs=[]
    out=0

    for x in set(val):
        occs.append(val.count(x))
        out = x if val.count(x)==2 and x>out else out

    return out if occs.count(2)==2 else 0

def one_pairs(hand):
    
    suits,val = split_hands(hand)

    occs=[]

    for x in set(val):
        if val.count(x)==2:
            return x

    return 0

def high_card(hand):
    suits,val = split_hands(hand)

    return max(val) 

wins = 0

for hand in hands:
    player_1 = hand[:5]
    player_2 = hand[5:]

    outcome_1=[
        royal(player_1),
        straight_flush(player_1),
        four_kind(player_1),
        full_house(player_1),
        flush(player_1),
        straight(player_1),
        three_kind(player_1),
        two_pairs(player_1),
        one_pairs(player_1),
        high_card(player_1)
    ]

    outcome_2=[
        royal(player_2),
        straight_flush(player_2),
        four_kind(player_2),
        full_house(player_2),
        flush(player_2),
        straight(player_2),
        three_kind(player_2),
        two_pairs(player_2),
        one_pairs(player_2),
        high_card(player_2)
    ]

    for n in range(len(outcome_1)):
        if (outcome_1[n]>outcome_2[n]):
            wins=wins+1
            break
        elif (outcome_1[n]<outcome_2[n]):
            break
print(wins)