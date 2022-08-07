N = int(input("N : "))
if N % 4 == 0:
    N += 1
else:
    N -= 1
print(N)