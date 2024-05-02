from functools import cmp_to_key

def compare(a, b):
    if len(a) == len(b):
        return 1
    return len(a) - len(b)

def solution(phone_book):
    a = phone_book
    a.sort()          
    answer = True

    for i in range(len(a)-1):
        c = a[i+1][0:len(a[i])]
        if a[i] == c:
            return False
    return answer

a = ["119", "97674223", "1195524421"]
print(solution(a))
