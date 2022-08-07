T = int(input())
for i in range(T):
    A = int(input())
    B = int(input())
    min = 0
    if A <= B:
        min = A
    else:
        min = B
    for j in range(1, min + 1):
        if A % j == 0 and B % j == 0:
            gcd = j
    print(gcd, sep = " ")
    lcm = (A * B) // gcd
    print(lcm)

