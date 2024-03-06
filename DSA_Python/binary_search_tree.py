


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return #node already exist

        if data < self.data: 
            if self.left: #insert into left subtree
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else: 
            if self.right: #insert into right subtree
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []
        
        if self.left: #visit left subtree
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right: #visit right subtree
            elements += self.right.in_order_traversal()

        return elements

    def search(self,val):
        if val == self.data:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def delete(self,val):
        if val < self.data:
            if self.data:
                self.left = self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.left is None and self.right is None:
                return None

            if self.left is None:
                return self.right

            if self.right is None:
                return self.left
                
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    numbers = [ 19, 1, 4, 9, 17, 18, 20, 23, 34]
    root =build_tree(numbers)

    print(root.in_order_traversal())
    print(root.search(17))
    print(root.search(89))
    root.delete(18)
    print(root.in_order_traversal())
    
