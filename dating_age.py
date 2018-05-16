def allowed_dating_age(my_age):  # function definition
    girls_age = my_age / 2 + 7
    return girls_age  # girls_age is returned in output


kevin = allowed_dating_age(24)  # function call and storing in variable

clinton = allowed_dating_age(29)

print("Kevin's Limit of dating:", kevin, "or older")

print("Clinton's Limit of dating:", clinton, "or older")
