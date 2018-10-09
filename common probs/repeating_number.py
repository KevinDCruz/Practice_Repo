def printRepeating(arr, size):
    print(" The repeating elements are", sep=" ")

    for i in range(size):

        if (arr[abs(arr[i])] > 0):
            arr[abs(arr[i])] = (-1) * arr[abs(arr[i])]
        else:
            print(abs(arr[i]), end=" ")

        # Driver code


arr = [1,2,3,2,1,4,6,5,5]
arr_size = len(arr)
print("Array size is:", arr_size)
printRepeating(arr, arr_size)