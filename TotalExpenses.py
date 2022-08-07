T = int(input())
for i in range(T):
    q = int(input())
    p = int(input())
    T = p * q
    if T > 1000:
        print(T - (T / 10))
    else:
        print(T)
