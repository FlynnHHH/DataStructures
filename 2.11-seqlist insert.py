va = list(map(int, input().split()))
x = int(input())
for i in range(len(va)):
    if va[i] > x:
        va.insert(i, x)
        break
    elif i == len(va) - 1:
        va.append(x)
print(*va)