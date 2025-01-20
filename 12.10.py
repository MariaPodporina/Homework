N=int(input('N:'))
nums=[]
for i in range(N):
    j=int(input())
    nums.append(j)
C=int(input("C:"))
def find_closest_sum(nums, target):
    closest_combination = None
    closest_sum = float('inf')
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    current_combination = (nums[i], nums[j], nums[k], nums[l])
                    current_sum = sum(current_combination)
                    if abs(current_sum - target) < abs(closest_sum - target):
                        closest_sum = current_sum
                        closest_combination = current_combination
    return list(closest_combination), closest_sum
print(find_closest_sum(nums,C))