from functools import cmp_to_key


def compare(a, b):
    return int(a + b) - int(b + a)


def solution(numbers):
    li = []
    st = ""
    for i in numbers:
        li.append(str(i))

    li.sort(key=cmp_to_key(compare),reverse=True)
    for i in li:
        st += i

    return st

numbers=[3,7,345,8897,12,43,131]
print(solution(numbers))



