def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)


for position in range(0, 12):
    print(get_fib(position))
