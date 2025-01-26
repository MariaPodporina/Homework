def is_valid_parentheses(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if stack and stack[-1] == pairs[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

def longest_valid_substring(s):
    max_length = 0
    start = -1
    stack = []
    last_index = -1

    for i, char in enumerate(s):
        if char in '({[':
            stack.append(i)
        else:
            if stack:
                stack.pop()
                if stack:
                    current_start = stack[-1]
                else:
                    current_start = last_index
                current_length = i - current_start
                if current_length > max_length:
                    max_length = current_length
                    start = current_start + 1
            else:
                last_index = i
    return s[start:start + max_length] if max_length > 0 else False

s = input().strip()
if is_valid_parentheses(s):
    print(True)
else:
    result = longest_valid_substring(s)
    print(result)
