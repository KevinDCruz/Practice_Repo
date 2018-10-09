#Palindrome

def palindrome(str1):
    if len(str1) > 0:
        str1 = str1.lower()
        str2 =str1[::-1]
        if str1 == str2:
            print("Palindrome")
        else:
            print("Not palindrome")
    else:
        return None

str1="MAdam"
palindrome(str1)
