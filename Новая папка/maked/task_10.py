def find_shortest_word_length(s):
    m = 999
    s = s.split()
    for i in s:
        if len(i) < m:
            m = len(i)
    return m

