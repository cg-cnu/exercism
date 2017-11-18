def calculate(text_input):
    flat_list = ''.join([i.lower() for sublist in text_input for i in sublist])
    chars = list(set([char for char in flat_list if char.isalpha()]))
    count = map(flat_list.count, chars)
    return dict(zip(chars, count))