list = [1,1,2,1,3,4,5,7,8,9,4,6,5]
set = set()
dups = []
for i in range(len(list)):
    set.add(list[i])
if len(list) == len(set):
    print("No Duplicate Values")
else:
    print("Duplicate Values Present")
print("Unique Values are:", *set)
sorted(list)
#Print Duplicate Values:

for j in range(len(list)):
    if list[j] in set:
        list.pop(j)

print("Duplicate numbers in list are:", list)
