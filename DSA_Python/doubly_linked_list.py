

class Node:
    def __init__(self, data = None, next = None, prev = None ):
        self.data = data
        self.next = next
        self.prev = prev

class Linkedlist:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Linkedlist is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linkedlist is empty")
            return

        itr = self.get_last_node()
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.prev else str(itr.data)
            itr = itr.prev
        print(llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_begining(self,data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head,None)
            self.head.prev = node
            self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None, None)
            return

        itr = self.head 
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            node = self.insert_at_begining(data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next= itr.next.next
                itr.next.prev = itr
                
            itr = itr.next
            count += 1
    def insert_values(self,data_list):
        for data in data_list:
            self.insert_at_end(data)
    
if __name__ == "__main__":  
    ll = Linkedlist()
    ll.insert_at_begining(3)
    ll.insert_at_begining(2)
    ll.insert_at_begining(1)
    ll.insert_at_end(6)
    ll.insert_at(3,5)
    ll.insert_at(3,4)
    ll.print_forward()
    ll.print_backward()
    ll.remove_at(4)
    ll.print_forward()
    ll.print_backward()
    ll.insert_values([7,8,9,10])
    ll.print_forward()
    ll.print_backward()
    