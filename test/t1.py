def t1(i):
    if i > 10:
        return i

    i += 1
    return t1(i)


print(t1(1))

