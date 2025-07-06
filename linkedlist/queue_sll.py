class Student:
    def __init__(self, id=0, name='', marks=0.0):
        self.id = id
        self.name = name
        self.marks = marks

    def __str__(self):
        return f'ID= {self.id}, Name= {self.name}, Marks= {self.marks}'


class Node:
    def __init__(self, student=None):
        self.data = student
        self.link = None

    def create_student(self):
        id = int(input('Enter ID of the student: '))
        name = input('Enter Name of the student: ')
        marks = float(input('Enter Marks of the student: '))
        student = Student(id, name, marks)
        return student


class Queue:
    def __init__(self):
        self.front = None

    def insert(self):
        node = Node()
        student = node.create_student()
        node.data = student
        if self.front is None:
            self.front = node
        else:
            node.link = self.front
            self.front = node
        print("Student inserted into queue.\n")

    def delete(self):
        if self.front is None:
            print("Queue is empty\n")
            return

        if self.front.link is None:
            print(f'Deleted Node data is: {self.front.data}\n')
            self.front = None
            return

        temp = self.front
        while temp.link.link is not None:
            temp = temp.link

        print(f'Deleted Node data is: {temp.link.data}\n')
        temp.link = None

    def display(self):
        if self.front is None:
            print("Queue is empty\n")
            return
        print("Queue contents:")
        temp = self.front
        while temp is not None:
            print(temp.data)
            temp = temp.link
        print()

if __name__ == "__main__":
    q = Queue()
    while True:
        print("1. Insert\n2. Delete\n3. Display\n4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            q.insert()
        elif choice == 2:
            q.delete()
        elif choice == 3:
            q.display()
        elif choice == 4:
            break
        else:
            print("Invalid choice\n")
