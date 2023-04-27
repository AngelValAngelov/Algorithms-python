def bubble_sort(nums):
    for index in range(len(nums)):
        for next_idx in range(len(nums) - 1):
            if nums[next_idx] > nums[next_idx + 1]:
                nums[next_idx], nums[next_idx + 1] = nums[next_idx + 1], nums[next_idx]
    return ' '.join(map(str, nums))


numbers = [int(n) for n in input().split()]

print(bubble_sort(numbers))
