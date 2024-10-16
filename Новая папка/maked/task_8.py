def create_phone_number(a:list):
    c = []
    for i in a:
        c.append(str(i))
    b = ''.join(c)
    print(a)
    return f'({b[0:3]}) {b[3:6]}-{b[6:10]}'
