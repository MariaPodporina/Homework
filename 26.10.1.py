R=input()
input_list = [int(num.strip()) for num in R[1:-1].split(',')]
def f(nums):
    def backtrack(path, remaining):
        if not remaining:
            result.append(path)
            return
        seen = set()
        for i in range(len(remaining)):
            if remaining[i] not in seen:
                seen.add(remaining[i])
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])

    result = []
    backtrack([], nums)
    return result
print(f(input_list))