class Parent:
    def print_last_name(self):
        print("D'Cruz")


class Child(Parent):

    def print_first_name(self):
        print("Kevin")

    def print_last_name(self): #Function Overwriting
        print("D'Souza")


kevin = Child()
kevin.print_first_name()
kevin.print_last_name()
