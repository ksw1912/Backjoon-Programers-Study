n = int(input())
li =[]
for _ in range(n):
    li.append(list(map(int, input().split())))
li.sort(key=lambda x: (x[1], x[0]))
for x,y in li:
    print(x,y)