T = int(input("T : "))
for i in range(T):
    A = int(input("A : "))
    B = int(input("B : "))
    if A > B:
        print("Minimum : ", A)
    else:
        print("Minimum : ", B)
    print("Maximum : ", A+B)