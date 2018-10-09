name, place, age = ['Kevin', 'Dartmouth', 24]
print("Name is " + name)
print("Place is " + place)
print("Age is " + str(age))


def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)


drop_first_last([75, 78, 54, 62, 98, 63, 86])
