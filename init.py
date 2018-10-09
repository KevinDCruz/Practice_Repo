"""class Tuna:

    def __init__(self):
        print("I'm a Tuna")

    def swim(self):
        print("I want to swim")


flipper = Tuna()
flipper.swim()

"""


class Enemy:

    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)


jason = Enemy(100)  # 100 gets assigned to x
sandy = Enemy(200)

jason.get_energy()
sandy.get_energy()
