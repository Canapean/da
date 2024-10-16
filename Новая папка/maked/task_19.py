def order_words(s:str):
    s = s.split()
    out = []
    for i in s:
        for j in i:
            if j.isdigit():
                out.insert(int(j),i)
    return ' '.join(out)



    


