#long seq
a = [i for i in range(2,1002)]

for c in a:
    if c % 2 == 0:
        print(c)
    else:
        print(c*(-1))


