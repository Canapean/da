def spin_words(s):
    b = s.split()
    c = []
    for i in range(len(b)):
        if len(b[i]) >= 5:
            b[i] = b[i][::-1]
    return ' '.join(b)
