class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class SLL:
    def __init__(self):
        self.head = None

    def insert_sorted(self, data):
        new_node = Node(data)
        if self.head is None or self.head.data > data:
            new_node.link = self.head
            self.head = new_node
        else:
            temp = self.head
            while temp.link and temp.link.data < data:
                temp = temp.link
            new_node.link = temp.link
            temp.link = new_node

    def display(self):
        temp = self.head
        print("List:", end=" ")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.link
        print("None")

def merge_sorted_lists(head1, head2):
    dummy = Node(0)
    tail = dummy
    while head1 and head2:
        if head1.data < head2.data:
            tail.link = head1
            head1 = head1.link
        else:
            tail.link = head2
            head2 = head2.link
        tail = tail.link

    if head1:
        tail.link = head1
    elif head2:
        tail.link = head2
    return dummy.link

# Driver code
if __name__ == "__main__":
    list1 = SLL()
    list2 = SLL()

    print("Enter elements for List 1 (sorted):")
    for val in [1, 3, 5]:
        list1.insert_sorted(val)

    print("Enter elements for List 2 (sorted):")
    for val in [2, 4, 6]:
        list2.insert_sorted(val)

    print("List 1:")
    list1.display()
    print("List 2:")
    list2.display()

    print("Merged Sorted List:")
    merged_head = merge_sorted_lists(list1.head, list2.head)

    temp = merged_head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.link
    print("None")
