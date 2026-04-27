def biggest_absolute(a, b, c, d):
    return max([a, b, c, d], key=abs)

print(biggest_absolute(3, -12, 5, 1))
