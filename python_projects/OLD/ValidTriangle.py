from copy import copy


def is_triangle(a, b, c):
    arr = [a, b, c]
    d = max(arr)
    arr.remove(d)
    return sum(arr) > d