def long_string(s):
    index = {}
    start = 0
    length=0
    lstr = ""
    for end in range(len(s)):
        if s[end] in index:
            start = max(start, index[s[end]] + 1)
        index[s[end]] = end
        if end - start + 1 > length:
            length = end - start + 1
            lstr = s[start:end + 1]
    return lstr
print(long_string(input()))
