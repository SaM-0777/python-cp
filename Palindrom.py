T = int(input())
for i in range(T):
    N = int(input())
    k1 = N;
    k2 = 0;
    while(k1 > 1):
        k2 = 10 * k2 + (k1 % 10)
        k1 = k1 // 10
    if k2 == N:
        print("Winner")
    else:
        print("Looser")

