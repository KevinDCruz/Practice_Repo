class Mario:
    def move(self):
        print("I'm Moving!")


class Shroom:
    def eat_shroom(self):
        print("Now, I'm Big")


class BigMario(Mario, Shroom):
    pass


bm = BigMario()
bm.move()
bm.eat_shroom()
