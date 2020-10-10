reached = False

def is_monotonic(n):
    digits = [int(i) for i in str(n)]

    is_inc = True
    is_dec = True

    size = len(digits)

    for i in range(size-1):
        if digits[i] > digits[i+1]:
            is_inc = False

        if digits[size-i-1] > digits[size-i-2]:
            is_dec = False

    if is_inc: return is_inc
    if is_dec: return is_dec
    return False
    
def get_first_inst(prop):
    n=1
    bouncy = 0
    while not reached:
        if not is_monotonic(n):
            bouncy+=1

        if bouncy/n == prop:
            return n
        n+=1

prop = 0.99
print(get_first_inst(prop))

