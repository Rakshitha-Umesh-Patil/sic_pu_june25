class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class SLL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.link:
                temp = temp.link
            temp.link = new_node

    def display(self):
        temp = self.head
        print("List:", end=" ")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.link
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.link
            current.link = prev
            prev = current
            current = next_node
        self.head = prev
        print("List reversed.")

if __name__ == "__main__":
    sll = SLL()
    while True:
        print("\n1. Insert\n2. Display\n3. Reverse\n4. Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            val = int(input("Enter value: "))
            sll.insert(val)
        elif ch == 2:
            sll.display()
        elif ch == 3:
            sll.reverse()
        elif ch == 4:
            break
        else:
            print("Invalid choice.")
