def count_vowels(string:str) -> int:
    a = ('a','e','i','o','u')
    count = 0
    for i in string:
        if i in a:
            count += 1
    return count
