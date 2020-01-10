a,b = 1,2
b,a = a,b
print(a, b)

seq = [(1,2,3), (4,5,6), (7,8,9)]
for a, b, c in seq:
    print(f"a={a},b={b},c={c}")

values = (1,2,3,4,5,6,7)
a,b, *_ = values
print(a, b)
print(_)

a = (1,2,2,3,3,3,4,5,8,8,9)
print(a.count(3))