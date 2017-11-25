def hey(phrase):
    import re
    phrase = phrase.strip()

    phrase_str = "".join([i for i in phrase if i.isalpha()])
    shout = re.compile('^[A-Z]+$')
    if shout.match(phrase_str):
        return "Whoa, chill out!"

    question = re.compile(r'.*?\?$')
    if question.match(phrase.strip()):
        return "Sure."

    phrase_str = "".join([i for i in phrase if i.isalnum()])
    if " ".join(phrase_str.split()) == " " or phrase_str == "":
        return "Fine. Be that way!"

    return "Whatever."