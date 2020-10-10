import itertools

nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

perms = list(itertools.permutations(nums))

sols=[]

for K in range(6, 27):

    for perm in perms:

        [a1, a2, a3, a4, a5, b, c1, c2, c3, c4]=perm
        if(a1+b+c1==K and 
            a2+c1+c2==K and
            a3+c2+c3==K and
            a4+c3+c4==K and
            a5+c4+b==K):

            a1=str(a1)
            a2=str(a2)
            a3=str(a3)
            a4=str(a4)
            a5=str(a5)
            c1=str(c1)
            c2=str(c2)
            c3=str(c3)
            c4=str(c4)
            b=str(b)

            a = [a1, a2, a3, a4, a5]
            a = [int(x) for x in a]

            start=0

            if(int(a1)==min(a)):
                start=0
            elif(int(a2)==min(a)):
                start=3
            elif(int(a3)==min(a)):
                start=6
            elif(int(a4)==min(a)):
                start=9
            elif(int(a5)==min(a)):
                start=12
            
            out_arr=[a1, b, c1, a2, c1, c2, a3, c2, c3, a4, c3, c4, a5, c4, b]

            out_arr=out_arr[start:]+out_arr[:start]

            out=''

            for val in out_arr:
                out=out+val

            if(len(out)==16):
                sols.append(int(out))

print(max(sols))