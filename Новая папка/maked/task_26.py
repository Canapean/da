def validate_ip(s):
    t = []
    s = s.split('.')
    if len(s) == 4:
        t.append('True')
        for i in s:
            if 0 <= int(i) <= 255:
                t.append('True')
    if len(t) == 5:
        return 'Yes'
    else:
        return 'No'