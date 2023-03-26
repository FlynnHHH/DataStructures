def fib(k, m):
    if m <= k:
        if m <= k - 2:
            return 0
        else:
            return 1
    else:
        return 2 * fib(k, m - 1) - fib(k, m - k - 1)

k, m = map(int, input().split())
print(fib(k, m))