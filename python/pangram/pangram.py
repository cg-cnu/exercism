def is_pangram(sentence):
    sentence = [char.lower() for char in sentence if char.isalpha()]
    return len(set(sentence)) == 26
