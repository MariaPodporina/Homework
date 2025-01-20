R=input()
R = [element.strip('"') for element in R[1:-1].split(', ')]
def group_strings(strings):
    groups = {}
    for s in strings:
        key = (tuple(sorted(s)), len(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())
print(group_strings(R))
