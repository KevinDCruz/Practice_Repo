str1 = []
str2 = {}

def non_repeating(string):
    for i in string:
        if i in str2:
            str2[i] = str2[i] + 1
        else:
            str2[i] = 1
            str1.append(i)

    for j in str1:
        if str2[j]==1:
            return j
    return None



string = "abaabbccdeeffewdef"
print(non_repeating(string))
