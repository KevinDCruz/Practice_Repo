#Check if two String is a rotation of each other

def rotation(str1, str2):
    if len(str1) == len(str2):
        temp =str1+str1
        if temp.count(str2) > 0:
            print("Is a rotation")
        else:
            print("Not a Rotation")
    else:
        print("Not a Rotation")



str1 = "ABCD,AV"
str2 = "CD,AVAB"
rotation(str1, str2)
