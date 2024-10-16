def solution(a,b):
    c = len(b)
    d = len(a)
    return True if b == a[d-c:d] else False
