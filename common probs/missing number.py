def missing_no(list):
    length = len(list)
    if length> 0:
        value1 = (length*(length+1))/2
        total = sum(list)
        missing = total - value1
        print(int(missing))
    else:
        return 0

A = [1,2,4,5,6]
missing_no(A)