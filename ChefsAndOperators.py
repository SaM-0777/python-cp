T = int(input("Total Test Cases : "))
for i in range(T):
    A = int(input("A : "))
    B = int(input("B : "))
    if A > B:
        print(">")
    elif A < B:
        print("<")
    else:
        print("=")