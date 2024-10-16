def check_case_match(a:str,b:str) -> int:
    if a.isupper() and b.isupper() or a.islower() and b.islower():
        return 1
    elif a.islower() and b.isupper() or b.islower() and a.isupper():
        return 0
    else:
        return -1
