def decode(string):
    import re
    c = re.split("([0-9]+)([A-Z])", string)
    c = [i for i in c if i != '']
    print c
    d = ''
    for i in c:
        if re.search("[0-9]", i):
            x = int(i)
            d * x 
        else:
    print d 

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

    strng = ''
    for j in final:
        if len(j) == 1:
            strng += j[0]
        else:
            strng += str(len(j)) + j[0]
    return strng
