def add_binary(a,b):
    c = (a+b)
    d = str(bin(c))
    return f'{a} + {b} = {c} in decimal or {d[2::]} in binary'
