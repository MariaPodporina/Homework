def generate_unique_subsets(elements):
    elements=list(set(elements)&set(elements))
    unique_subsets = set()
    def backtrack(start, current_subset):
        if current_subset:
            unique_subsets.add(tuple(sorted(current_subset)))
        for i in range(start, len(elements)):
            current_subset.append(elements[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()
    backtrack(0, [])
    result = [set(subset) for subset in unique_subsets]
    return result, len(result)

list1 = [1, 2, 3, 4]
subsets2, count2 = generate_unique_subsets(list1)
print("Подмножества:", subsets2)
print("Количество подмножеств:", count2)
