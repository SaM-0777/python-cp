T = int(input())
for i in range(T):
    length = int(input())
    A = [length]
    for j in range(length):
        A.append(int(input()))
    sum = 0
    if length <= 2:
        for k in range(length):
            sum += A[k]
        print(sum)
        break
    prev = A[0] + A[1]
    for x in range(length):
        for y in range(length):
            if x == y:
                continue
            sum = A[x] + A[y]
            if sum < prev:
                prev = sum
    print(prev)
