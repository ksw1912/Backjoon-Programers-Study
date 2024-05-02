ex = [35, 1, 2, 5, 9, 677, 5, 8, 3, 132, 1]


def Quick_Sorted(ex):
    for i in range(len(ex) - 1):
        for j in range(len(ex) - i - 1):
            if ex[j] > ex[j + 1]:
                ex[j], ex[j + 1] = ex[j + 1], ex[j]
    return ex


def Merge_Sorted(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]

    left = Merge_Sorted(left)
    right = Merge_Sorted(right)
    return Merge(left, right)


def Merge(left, right):
    i = 0
    j = 0
    total = []
    while (i < len(left) and j < len(right)):
        if left[i] < right[j]:
            total.append(left[i])
            i += 1
        else:
            total.append(right[j])
            j += 1
    while (i < len(left)):
        total.append(left[i])
        i += 1
    while (j < len(right)):
        total.append(right[j])
        j += 1
    return total


# Quick Sorted
print(Quick_Sorted(ex))
print(Merge_Sorted(ex))
