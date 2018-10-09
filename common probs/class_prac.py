class DBIT:

    whiskey = "DSP Black" #Class Variable
    def __init__(self, name):
        self.name = name #Instance Variable
        self.girl = []

    def add_girl(self, girls):
        self.girl.append(girls)

Kevin = DBIT("Kevin")
Pinto = DBIT("Clinton")
Kevin.add_girl("Ivonne")
Pinto.add_girl("Forever Alone")
Pinto.add_girl("Get one soon, bro")



class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)



obj1 = Bag("ka")
obj1.add("Hoel")
obj1.addtwice("Again Hoel")
print(Obj1.data())