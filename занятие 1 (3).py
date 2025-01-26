def perfect(m, n):
    if n == 1:
        return m
    r = [''] * n
    l, step = 0, 1
    for k in m:
        r[l] += k
        if l == 0:
            step = 1
        elif l == n - 1:
            step = -1
        l += step
    return ''.join(r)
word = input('word ')
number = int(input('number '))
print(perfect(word, number))
