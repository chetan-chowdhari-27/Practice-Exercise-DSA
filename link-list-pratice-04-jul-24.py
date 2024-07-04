class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkList:
    def __init__(self):
        self.head = None
    
    def insert_in_begining(self, data):
        node = Node(data, self.head)
        self.head = node


    def insert_in_end(self, data):
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def print_ll(self):
        itr = self.head
        lstr = ''
        while itr:
            if itr.next is not None:
                lstr += str(itr.data) + '-->'
            else:
                lstr += str(itr.data)
            itr = itr.next
        print(lstr)
    
    def get_length(self):
        count = 0 
        itr = self.head
        while itr:
            count += 1 
            itr = itr.next
        return count


if __name__ == "__main__":
    llist = LinkList()
    llist.insert_in_begining(32)
    llist.insert_in_end(23)
    llist.insert_in_begining(2)
    llist.insert_in_begining(4)
    # print(llist.get_length())
    llist.print_ll()
