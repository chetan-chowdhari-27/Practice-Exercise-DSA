# creating  Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# creating  Linklist
class LinkList:
    # Initializing Empty values
    def __init__(self):
        self.head = None

    # create Insert into Begining     
    def insert_in_biggining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # create into end of linklist 
    def insert_at_end(self, data):
        new_node = Node(data)
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        
    # remove from end 
    def remove_list_end(self):
        current = self.head
        if current.next is None:
            self.head = None 
            return

        while current.next.next is not None:
            current = current.next

        current.next = None 

    # create into specific index 

    
    # printing the linklist    
    def print_ll(self):
        current = self.head
        while current:
            if current.next  is not None:
                print(current.data, '-->', end=" ")
            else:
                print(current.data, end=" ")                
            current = current.next
        print()


if __name__ == '__main__':
    llist = LinkList()
    llist.insert_in_biggining(2)
    # llist.insert_at_end(112)
    llist.insert_in_biggining(6)
    llist.insert_in_biggining(7)
    llist.insert_in_biggining(5)
    llist.insert_in_biggining(100)    
    # llist.insert_at_end(12)
    llist.remove_list_end()
    llist.print_ll()


# excercise -> Merge Two Sorted List

