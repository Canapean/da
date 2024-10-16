def remove_vowels(string):
    fu = ('a','e','i','o','u','A','E','I','O','U')
    b = []
    for i in string:
        if i not in fu:
            b.append(i)
    return ''.join(b)


