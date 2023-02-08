def array_sum(nums, idx):
    if idx == len(nums) - 1:
        return nums[idx]
    return nums[idx] + array_sum(nums, idx + 1)


list_numbers = list(map(int, input().split()))

print(array_sum(list_numbers, 0))
