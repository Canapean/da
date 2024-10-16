def find_uniq(a):
    b = 0
    if a[0] == a[1]:
        for i in a:
            if i != a[0]:
                b = i
    elif a[0] != a[1] and a[0] != a[2]:
        b = a[0]
    elif a[0] != a[1] and a[1] != a[2]:
        b = a[1]
    return b
