from itertools import permutations
value,compare=input().split()
compare=int(compare)
a=str(value)
a=''.join(sorted(a))
# print(a)
b=str(compare)
if(len(a)<len(b)):
    print(-1)
else:
    result=-1
    permlist=permutations(a)
    for i in list(permlist):
        str1=''.join(i)
        n=int(str1)
        if(n>compare):
            result=n
            break
    print(result)


