class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.start = None

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.start
        self.start = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
        else:
            current = self.start
            while current.next is not None:
                current = current.next
            current.next = new_node

    def delete_from_start(self):
        if self.is_empty():
            print("List is empty. Cannot delete.")
        else:
            self.start = self.start.next

    def delete_from_end(self):
        if self.is_empty():
            print("List is empty. Cannot delete.")
        elif self.start.next is None:
            self.start = None
        else:
            current = self.start
            while current.next.next is not None:
                current = current.next
            current.next = None

    def search(self, value):
        current = self.start
        while current is not None:
            if current.data == value:
                return True
            current = current.next
        return False

    def display(self):
        if self.is_empty():
            print("List is empty.")
        else:
            current = self.start
            while current is not None:
                print(current.data, end=" -> ")
                current = current.next
            print("None")
# here insert the new node in betweeen node 
    def insert_at_position(self, data, position):
        if position < 1:
            print("Position must be 1 or greater.")
            return
        new_node = Node(data)
        if position == 1:
            new_node.next = self.start
            self.start = new_node
        else:
            current = self.start
            count = 1
            while current is not None and count < position - 1:
                current = current.next
                count += 1
            if current is None:
                print("Position is out of bounds.")
            else:
                new_node.next = current.next
                current.next = new_node


# Example of using the class
sll = SLL()
sll.insert_at_start(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.insert_at_end(100)
sll.display()  # Output: 10 -> 20 -> 30 -> 100 -> None
sll.delete_from_start()
sll.display()  # Output: 20 -> 30 -> 100 -> None
sll.delete_from_end()
sll.display()  # Output: 20 -> 30 -> None
print(sll.search(20))  # Output: True
print(sll.search(40))  # Output: False

sll.insert_at_position(15, 2)
sll.display()  # Output: 20 -> 15 -> 30 -> None

sll.insert_at_position(5, 1)
sll.display()  # Output: 5 -> 20 -> 15 -> 30 -> None

sll.insert_at_position(50, 6)
sll.display()  # Output: 5 -> 20 -> 15 -> 30 -> 50 -> None
