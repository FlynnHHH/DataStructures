x, y, z = map(int, input().split())
lst = [x, y, z]
lst.sort(reverse=True)
print(lst[0], lst[1], lst[2])