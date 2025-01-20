def letters(number):
    alphabet={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total=0
    past=0
    for current in reversed(number):
        current_value = alphabet[current]
        if current_value < past:
            total -= current_value
        else:
            total += current_value
        past = current_value
    return total
print(letters(input()))