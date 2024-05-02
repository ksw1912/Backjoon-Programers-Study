N = int(input())
count = 0
X = {}
Y = {}
for i in range(N):
    car = input()
    X[car] = i 

for i in range(N):
    car = input()
    Y[car] = i 

for i in X:
    for j in X:
        if X[i] > X[j] and Y[i] < Y[j]:
            count+=1
            break
print(count)



