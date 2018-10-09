def print_pairs(arr, val1):
    s = set()

    for i in range(len(arr)):
        val2=val1-arr[i]
        if val2 >=0 and val2 not in s:
            print("Pairs include: ", arr[i], "and", val2)
            s.add(arr[i])
        else:
            return 0



arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
val1=16
print_pairs(arr, val1)