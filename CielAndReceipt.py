T = int(input("T : "))

for i in range(T):
    N = int(input())
    total = 0
    if N >= 100:
        total += N // 100
        N = N - ((N // 100) * 100)
    if N >= 50:
        total += N // 50
        N = N - ((N // 50) * 50)
    if N >= 10:
        total += N // 10
        N = N - ((N // 10) * 10)
    if N >= 5:
        total += N // 5
        N = N - ((N // 5) * 5)
    if N >= 2:
        total += N // 2
        N = N - ((N // 2) * 2)
    else:
        total += N

    print("Minimum Currencies : ", total)