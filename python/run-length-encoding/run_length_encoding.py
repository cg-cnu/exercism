
def decode(string):
    import re
    patterns = re.findall(r"(\d*)([A-z\s])", string)
    return "".join(int(n) * a if n else a for n, a in patterns)

def encode(string):
    from itertools import groupby
    encoded = ''
    for (char, count) in [(char, len(list(charG))) for char, charG in groupby(string)]:
        encoded += ('' if count == 1 else str(count) ) + char
    return encoded
