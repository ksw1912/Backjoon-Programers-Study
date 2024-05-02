import sys
input = sys.stdin.readline
n, m = map(int, sys.stdin.readline().rstrip().split())
s = set()
count = 0
for i in range(n):
    s.add(sys.stdin.readline().strip())
    
for i in range(m):
    x = sys.stdin.readline().rstrip()
    if x in s:
        count +=1
print(count)