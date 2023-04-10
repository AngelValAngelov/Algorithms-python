def recursive_factorial(num):
    if num == 1:
        return num
    return num * recursive_factorial(num - 1)


num = int(input())

print(recursive_factorial(num))
