for f in range(1, 16):
    if f % 5 == 0 and f % 3 == 0:
        print("Fizzbuzz")
    elif f % 5 == 0:
        print("Fizz")
    elif f % 3 == 0:
        print('Buzz')
    else:
        print(f)
