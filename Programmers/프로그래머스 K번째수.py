array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    answer = array
    li = []
    an = []
    for i, j, k in commands:
        li = answer[i - 1:j]
        li.sort()
        an.append(li[k - 1])

    return an


a = solution(array, commands)
print(a)
