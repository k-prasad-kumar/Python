
#General Tree 

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.childrens = []
        self.parent = None


    def add_child(self, child):
        child.parent = self
        self.childrens.append(child)

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + '|__ ' if self.parent else ""
        print(prefix + self.data)
        for child in self.childrens:
            child.print_tree()

    def get_level(self):
        parent = self.parent
        level = 0
        while parent:
            level +=1
            parent = parent.parent
        return level

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptops")
    laptop.add_child(TreeNode("Macbook"))
    laptop.add_child(TreeNode("Notebook"))
    laptop.add_child(TreeNode("Thinkpad"))

    mobile = TreeNode("Mobiles")
    mobile.add_child(TreeNode("iPhone"))
    mobile.add_child(TreeNode("Google Pixel"))
    mobile.add_child(TreeNode("Samsung"))

    tv = TreeNode("Telivisions")
    tv.add_child(TreeNode("OnePlus"))
    tv.add_child(TreeNode("Sony"))
    tv.add_child(TreeNode("Samsung"))

    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(tv)

    root.print_tree()

if __name__ == "__main__":
    build_product_tree()


