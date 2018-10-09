#Check if two Strings are anagrams of each other? (solution)

def check_anagrams(str1, str2):
    if sorted(str1)==sorted(str2):
        print("Strings are anagrams")
    else:
        print("Strings are not anagrams")


print("Enter String one: \n")
str1=input()
print("Enter String two: \n")
str2=input()
check_anagrams(str1, str2)


