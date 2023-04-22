def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2
        if numbers[middle] == target:
            return middle
        if numbers[middle] > target:
            right = middle - 1
        else:
            left = middle + 1

    return -1


numbers = [int(n) for n in input().split()]
target = int(input())

print(binary_search(numbers, target))
