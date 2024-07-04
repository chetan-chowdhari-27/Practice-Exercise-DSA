import __main__


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_bigining(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def print(self):
        itr = self.head
        llstr = ''
        while itr:
            suffix = ''
            if itr.next:
                suffix = '-->'
            llstr += str(itr.data) + suffix
            itr = itr.next
        print(llstr)

    def get_lenght(self):
        count = 0 
        itr = self.head
        while itr:
            count += 1 
            itr = itr.next
        return count
    
    def insert_dat_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return   
          
        itr  = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

#  to insert some value in the specific location
    def insert_at(self, index, data):
        if index < 0 or index > self.get_lenght():
            raise Exception("Invalid Index ")
        if index == 0:
            self.insert_at_bigining(data)
            return 
        
        itr = self.head
        count = 0 
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break 
            itr = itr.next
            count += 1 

    def remove_at(self, index):
        if index < 0 or index > self.get_lenght():
           raise Exception("Invalid Index ")
         
        if index == 0:
           self.head.next
           return 
        
        itr = self.head
        count = 0 
        while itr:
            if count == index - 1: 
                itr.next = itr.next.next 
                break 

            itr = itr.next
            count += 1 

    def insert_values_in_list(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_dat_end(data)

if __name__ == '__main__':
    root = Linkedlist()
    # root.insert_dat_end(567)
    # root.insert_dat_end(99)
    # root.insert_dat_end(2332)
    # root.insert_at(2,40)
    root.insert_values_in_list(['banana','orange','apple', 'grapes'])
    root.insert_at(1,'BuleBerry')
    root.print()
    # root.remove_at(2)
    # root.print()

