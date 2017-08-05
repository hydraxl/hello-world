def hof(f, y):
    if y <= 0:
        return f
    else:
        return hof(lambda x: f(f(x)), y - 1)
add_one = lambda x: x + 1

print(hof(add_one, 3)(5))
