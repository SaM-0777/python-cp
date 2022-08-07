T = int(input())
for i in range(T):
    s = str(input())
    if len(s) < 2:
        print("No")
        break
    elif len(s) % 2 != 0:
        #pivot = s[len(s) // 2]
        left = s[: len(s) // 2]
        right = s[len(s) // 2 + 1 :]
        current_char = left[0]
        left_count = right_count = 0
        left_char = {left[0] : count}
        right_char = {right[0] : count}
        for j in range(len(left)):
            if left[j] == left[current_char]:
                left_count += 1
            else:
                current_char = left[j]
