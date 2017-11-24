def word_count(phrase):
    from collections import Counter
    import re
    pattern = re.compile(r"[a-zA-Z0-9]+(?:'\w)?")
    return Counter(pattern.findall(phrase.lower()))