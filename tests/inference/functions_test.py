
def f1(x):
    u = x[0]
    v = x * 3
    return u * v


def f2(x):
    return [x]


def f3(x):
    return x


def f4(x, y):
    u = x["string"] + y
    v = y + 3
    return u | v


def f5(x, y, i):
    t = x * 3
    u = y["string"]
    v = x[i]
    return (t[0] + v) * (u + 3)


def f7(x):
    return x["string"]


a = f1([1, 2, 3])
b = f2(a[0])
c = f3(b)
d = f4({"": c[0]}, 2)
e = f5(a, {"": 2j}, 2)
