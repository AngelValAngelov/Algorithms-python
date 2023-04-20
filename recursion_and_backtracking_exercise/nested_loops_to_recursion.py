def find_all_combination(idx, combination):
    if idx == len(combination):
        print(*combination, sep=' ')
        return
    for num in range(1, len(combination) + 1):
        combination[idx] = num
        find_all_combination(idx + 1, combination)


number = int(input())
combination = [1] * number

find_all_combination(0, combination)
