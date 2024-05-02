from functools import cmp_to_key 
count = int(input())
li=[]
lis =[]
def compare(x,y):
    if len(x) == len(y):
        if x>y: return 1
        else: return -1
    elif (len(x) > len(y)): return 1
    else : return -1


for i in range(count):
    li.append(input())

lis = list(set(li))

lis.sort(key = cmp_to_key(compare))

for i in lis:
    print(i)