# HHPHPPHHPPHPPPHPHPHP


n, k = map(int, input().split())
ham = input()
used = [False] * n
for i in range(n):
    if ham[i] == 'H':
        continue
    for j in range(max(0, i-k), min(n, i+k+1)):
        if ham[j] == 'H' and not used[j]:
            print("i = ", i, " ", j, "번 햄버거 ", "used[j] = ", used[j])
            print(used)
            print("먹을 수 있는 햄버거를 찾았으므로 break j loop\n")
            break
    else:
        print("j포문을 돌았으나 먹을 수 있는 햄버거가 없다 = else")
        print("i = ", i, " j = ", j, " used[j] = ", used[j])
        print(used, "\n")
        continue
    used[j] = True
    print("먹은 햄버거를 표시 change to true")
    print("i = ", i, " j = ", j, " used[j] = ", used[j])
    print(used, "\n")
print(sum(used))