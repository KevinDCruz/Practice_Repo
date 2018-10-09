#Missing Number
def missing(A):
    n = len(A)
    if n > 0:
        sum1 = (n)*(n+1)/2
        total = sum(A)
        return total-sum1
    else:
        return 0

A = [1,2,4,5,6]
print(int(missing(A)))

