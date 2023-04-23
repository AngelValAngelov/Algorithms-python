def insertion_sort(nums):
    for i in range(len(nums)):
        for j in range(i, 0, -1):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
            else:
                break
    return ' '.join(map(str, nums))


numbers = [int(n) for n in input().split()]

print(insertion_sort(numbers))
