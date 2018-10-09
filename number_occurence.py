x = 0
y = 5
z = 5
n = 5

## 9*19 + 7 + 9 + 81

counter = x * 19
if(x > n):
    counter = counter + 81

if (y > n):
    counter = counter + (y - 1) + 10
else:
    counter = counter + y - 1
if (z > n):
    counter = counter + 1
else:
    counter = counter

print(counter)
