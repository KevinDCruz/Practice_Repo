def flex(*args):
    total = 0
    for a in args:
        total += a
        print(total)


flex(3)
flex(5, 10)
flex(3, 32, 15)
