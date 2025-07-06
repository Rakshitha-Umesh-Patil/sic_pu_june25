class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

def get_intersection(head1, head2):
    def get_count(head):
        count = 0
        while head:
            count += 1
            head = head.link
        return count

    def advance(head, diff):
        for _ in range(diff):
            head = head.link
        return head

    c1 = get_count(head1)
    c2 = get_count(head2)

    if c1 > c2:
        head1 = advance(head1, c1 - c2)
    else:
        head2 = advance(head2, c2 - c1)

    while head1 and head2:
        if head1 == head2:
            return head1
        head1 = head1.link
        head2 = head2.link
    return None

if __name__ == "__main__":
    # Create list 1
    a1 = Node(10)
    a2 = Node(20)
    a3 = Node(30)
    a1.link = a2
    a2.link = a3

    
    b1 = Node(5)
    b2 = Node(15)
    b1.link = b2
    b2.link = a2  

    intersection = get_intersection(a1, b1)
    if intersection:
        print("Lists intersect at node with data:", intersection.data)
    else:
        print("Lists do not intersect.")
