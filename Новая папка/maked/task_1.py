t = ('+-+','--+')

def interact_strings(t):
    result = ''
    for i in range(len(t[0])):
        if t[0][i] + t[1][i] == '++':
            result += '+'
        elif t[0][i] + t[1][i] == '--':
            result += '-'
        elif t[0][i] + t[1][i] in ['+-','-+']:
            result += '0'
        else:
            pass
    return result
print(interact_strings(t))