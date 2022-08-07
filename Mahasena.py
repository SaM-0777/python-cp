N = int(input("N : "))
A = [N]
for i in range(N):
    A.append(int(input("Weapon Number : ")))
lucky = unlucky = 0
for i in range(N):
    if A[i] % 2 == 0:
        lucky += 1
    else:
        unlucky += 1
if lucky > unlucky:
    print("READY FOR BATTLE")
else:
    print("NOT READY")