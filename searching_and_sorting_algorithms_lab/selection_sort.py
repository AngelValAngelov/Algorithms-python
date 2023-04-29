def selection_sort(nums):
    length = len(nums)

    for index in range(length):
        next_index = index
        for n in range(index, length):
            if nums[n] < nums[next_index]:
                next_index = n
        nums[index], nums[next_index] = nums[next_index], nums[index]
    return ' '.join(map(str, nums))


numbers = [int(n) for n in input().split()]
print(selection_sort(numbers))
