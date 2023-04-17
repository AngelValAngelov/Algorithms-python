def fibonacci(number):
    # if number <= 1:
    #     return 1
    # return fibonacci(number - 1) + fibonacci(number - 2)
    index_1 = 1
    index_2 = 1
    result = 0
    for n in range(number - 1):
        result = index_1 + index_2
        index_1, index_2 = index_2, result

    return result


number = int(input())

print(fibonacci(number))
