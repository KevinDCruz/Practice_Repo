"""
kev = int(input("Enter your fav number: \n"))
print(kev)
"""
while True:
    try:
        kevin = int(input("Enter your favourite number: \n"))
        print(kev)
        break
    except ValueError:
        print("Enter a number")
