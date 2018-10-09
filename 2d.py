counter = 0
row = 6
column = 6
i = 0
j = 0
x = 3
y = 3
for i in range(0, row):
    if i + x <= row:
        for j in range(0, column):
            if j + y <= column:
                counter = counter + 1
print(counter)
