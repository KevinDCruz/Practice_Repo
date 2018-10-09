list = [1, 2, 3, 4, 5]
print("List")
for i in list:
    print(i)


"""tuple = (5, 10, 15, 20, 25, 30, 35, 15, 40, 20)
print("Tuple")
for j in tuple:
    print(j)

set = {10, 20, 30, 35, 40, 20, 15}
print("Set")
for k in set:
    print(k)
"""

squares = [num * num for num in list]
print(squares)

m = 4
for x in range(1, 10, 3):
    if x is m:
        print(x, "is chosen")
    else:
        print("Hey")
