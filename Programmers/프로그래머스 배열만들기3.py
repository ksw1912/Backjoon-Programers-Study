intervals= [[1,3],[0,4]]
arr= [1,2,3,4,5]
li =[]

for x,y in intervals:
    for j in range(x,y+1):
        li.append(arr[j])

print(li)
                



