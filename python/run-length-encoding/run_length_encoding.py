def decode(string):
    import re
    c = re.split("([0-9]+)([A-Z])", string)
    c = [i for i in c if i != '']
    d = []
    for i in c:
        try:
            i = int(i)
            d.append(i)
        except ValueError:
            d.append(i)


def encode(string):
    final = []
    cur = ''
    for index, i in enumerate(string):
        try:
            if i == string[index+1]:
                cur += i
            else:
                final.append(cur+i)
                cur = ''
        except IndexError:
            final.append(cur+i)
    # print final

    strng = ''
    for j in final:
        if len(j) == 1:
            strng += j[0]
        else:
            strng += str(len(j)) + j[0]
    return strng

# encode('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB')
decode('2AB3CD4E')