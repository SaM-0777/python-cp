T = int(input())
for i in range(T):
    N = int(input())
    c = 0
    for j in range(1, N):
        if N % j == 0:
            c += 1
    if c > 1:
        print("No")
    else:
        print("Yes")
