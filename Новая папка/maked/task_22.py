def likes(a:list):
    b = len(a)
    if b == 0:
        return 'no one likes this'
    elif b == 1:
        return f'{a[0]} likes this'
    elif b == 2:
        return f'{a[0]} and {a[1]} likes this'
    elif b == 3:
        return f'{a[0]}, {a[1]} and {a[2]} likes this'
    else:
        return f'{a[0]}, {a[1]} and {b-2} others like this'
