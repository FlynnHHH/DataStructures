n, arrsize = map(int, input().split())
MAXINT = 2 ** 32 - 1

def factorial(i):
    factorial = 1
    if i == 0:
        return 1
    else:
        for index in range(1, i+1):
            factorial *= index
        return factorial


if n > arrsize:
    print(-1)
else:
    a = []
    for k in range(n):
        a.append(factorial(k) * 2 ** k)
    if a[n - 1] <= MAXINT:
        print(*a)
    else:
        print(-1)
