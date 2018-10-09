

def vowel_consonant(string):
    vowels = 0
    consonants = 0
    digits = 0
    special_char = 0

    for i in range(len(string)):
        temp = string[i]
        if ((temp>= 'a' and temp <='z') or (temp>= 'A' and temp <='Z')):
            if ((temp=='a' or temp=='e' or temp=='i' or temp=='o' or temp =='u')):
                vowels = vowels + 1
            else:
                consonants = consonants + 1
        elif (temp >='0' and temp <='9'):
            digits = digits + 1
        else:
            special_char = special_char + 1
    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Digits:", digits)
    print("Special Characters:", special_char)

string = "Kevin is a Dickhead123!!!"
vowel_consonant(string)

