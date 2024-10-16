def count_bits(a:int):
    b = str(bin(a))[2:]
    c = 0
    for i in b:
        if i == '1':
            c += 1
    return c
