while True:
    try:
        number = int(input("Favourite number?\n"))
        print(10 / number)
        break
    except SyntaxError:
        print("Make sure and Enter a number")
