class Node:
    def __init__(self, data=0):
        if data == 0:
            data = int(input('Enter data of the node: '))
        self.left = None
        self.data = data
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        print('An empty BST is created')

    def add_node(self):
        new_node = Node()
        if self.root is None:
            self.root = new_node
            return
        temp1 = self.root
        temp2 = None
        while temp1 is not None:
            temp2 = temp1
            if new_node.data < temp1.data:
                temp1 = temp1.left
            else:
                temp1 = temp1.right
        if new_node.data < temp2.data:
            temp2.left = new_node
        else:
            temp2.right = new_node

    def in_order(self, temp):
        if temp is None:
            return
        self.in_order(temp.left)
        print(temp.data, end='  ')
        self.in_order(temp.right)

    def pre_order(self, temp):
        if temp is not None:
            print(temp.data, end='  ')
            self.pre_order(temp.left)
            self.pre_order(temp.right)

    def post_order(self, temp):
        if temp is None:
            return
        self.post_order(temp.left)
        self.post_order(temp.right)
        print(temp.data, end='  ')

    def search_node(self, temp, search_data):
        found = False
        if temp is not None:
            if temp.data == search_data:
                return True
            found = self.search_node(temp.left, search_data)
            if found:
                return found
            found = self.search_node(temp.right, search_data)
        return found

    def delete_node(self, temp, delete_data):
        if temp is None:
            return None

        if delete_data < temp.data:
            temp.left = self.delete_node(temp.left, delete_data)
        elif delete_data > temp.data:
            temp.right = self.delete_node(temp.right, delete_data)
        else:
            
            if temp.left is None and temp.right is None:
                return None
            elif temp.left is None:
                return temp.right
            elif temp.right is None:
                return temp.left
            else:
                successor = self.get_min(temp.right)
                temp.data = successor.data
                temp.right = self.delete_node(temp.right, successor.data)
        return temp

    def get_min(self, temp):
        while temp.left is not None:
            temp = temp.left
        return temp


class Menu:
    def __init__(self):
        self.choice = 0

    def is_tree_empty(self, bst):
        if bst.root is None:
            print('Tree is empty')
            return True
        return False

    def menu(self, bst):
        match self.choice:
            case 1:
                bst.add_node()
            case 2:
                if self.is_tree_empty(bst):
                    return
                search_data = int(input('Enter data of the node to be searched: '))
                found = bst.search_node(bst.root, search_data)
                if found:
                    print(f'Node with data {search_data} found')
                else:
                    print(f'Node with data {search_data} not found')
            case 3:
                if self.is_tree_empty(bst):
                    return
                print("Inorder Traversal:")
                bst.in_order(bst.root)
                print()
            case 4:
                if self.is_tree_empty(bst):
                    return
                print("Preorder Traversal:")
                bst.pre_order(bst.root)
                print()
            case 5:
                if self.is_tree_empty(bst):
                    return
                print("Postorder Traversal:")
                bst.post_order(bst.root)
                print()
            case 6:
                if self.is_tree_empty(bst):
                    return
                delete_data = int(input('Enter data of the node to be deleted: '))
                bst.root = bst.delete_node(bst.root, delete_data)
            case 7:
                self.choice = 0
            case _:
                print('Invalid choice')

    def start_app(self):
        bst = BST()
        while True:
            print('\n1:Add  2:Search  3:Inorder  4:PreOrder  5:PostOrder  6:Delete  7:Exit')
            self.choice = int(input('Enter your choice: '))
            self.menu(bst)
            if self.choice == 0:
                print('Application closed')
                break



menu = Menu()
menu.start_app()
