def words(input_string):
    words = input_string.split()
    words.reverse()
    if words:
        words[0] = words[0].capitalize()
        for i in range(1, len(words)):
            words[i] = words[i].lower()
    result = ' '.join(words)
    return result

print(words(input()))