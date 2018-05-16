def health_calculator(age, apples, beer):
    ans = (100 - age) + (apples * 3.5) - (beer * 2)
    print(ans)


list = [24, 2, 0]
health_calculator(list[0], list[1], list[2])
health_calculator(*list)
