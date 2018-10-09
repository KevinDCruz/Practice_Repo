
class node():
    def __init__(self, data=None):  # Data= data in the LL at the location
        self.data = data
        self.next = None  # pointer to next node


class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        total = 0
        cur = self.head
        while cur.next != None:
            total = total + 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("Enter Lower index")
            return None
        cur_idx = 0
        cur = self.head
        while True:
            cur = cur.next
            if cur_idx == index:
                return cur.data
            cur_idx = cur_idx + 1

    def erase(self, index):
        if index >= self.length():
            print("Error, enter lower index")
            return None
        cur_idx = 0
        cur = self.head
        while True:
            last_node = cur
            cur = cur.next
            if cur_idx == index:
                last_node.next = cur.next
                return
            cur_idx += 1


my_list = linked_list()
my_list.append(2)
my_list.append(10)
my_list.append(3)
my_list.display()
print("Element at position 2: %d" % my_list.get(2))
my_list.erase(1)
my_list.display()
