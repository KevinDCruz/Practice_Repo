class Girl:
    gender = 'female'  # Class Variable

    def __init__(self, name):
        self.name = name  # instance Variable


object1 = Girl('Juhi')
object2 = Girl('Sibbs')

print(object1.name)
print(object2.name)
print(object1.gender)
print(object2.gender)
