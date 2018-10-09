fw = open("sample4.txt", 'w')

fw.write("Writing in my text file\n")
fw.write("Bhoooola!\n")
fw.close()

fr = open("sample4.txt", 'r')
k = fr.read()
print(k)
