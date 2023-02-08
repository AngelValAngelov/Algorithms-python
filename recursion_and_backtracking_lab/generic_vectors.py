def generating_vectors(idx, vector):
    if idx == len(vector):
        print(*vector, sep='')
        return
    for n in range(2):
        vector[idx] = n
        generating_vectors(idx + 1, vector)


num = int(input())
vector = [0] * num

generating_vectors(0, vector)
