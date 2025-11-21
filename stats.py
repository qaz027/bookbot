def sort_on(items):
    return items["num"]

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_frequency(text):
    frequency = {}
    for s in text:
        s = s.lower()
        if s in frequency:
            frequency[s] += 1
        else:
            frequency[s] = 1
    return frequency

def create_sorted_dictionary(dictionary):
    
    sorted_list = []
    for key, value in sorted(dictionary.items()):
        if key.isalnum():  
            sorted_list.append({'char': key, 'num': value})

    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list
