
# Print duplicate characters from String? (solution)

str = "Kevin is a dickhead"

# Initialize dictionary and set value of all keys to zero
dic = {}
for i in str:
   dic[i] = 0

# Update char counts in the dictionary
for i in str:
   dic[i]+= 1    # char is used as the key and the value is the count of that char in the string repeated chars hash to the same position
print(dic)

# Print characters with count > 1
for i,count in dic.items():
   if count > 1 and i != ' ':
      print ("%c has occured %d times" % (i, count))

