class Node:
    """Represent single node"""

    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    """Creates a Linked List"""

    def __init__(self):
        print('Created a Linked List Object')
        self.head = None

    def __str__(self):
        if self.head is None:
            return 'Empty'
            # return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        if llstr != '':
            if llstr[-3:] == '-->':
                return llstr[:-3]
            else:
                return llstr

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        print(f'Inserted {data} at the beginning')

    def insert_at_end(self, data):
        if self.head is None:           # this means the linkedlist object has just been created and no element has been 
            self.insert_at_beginning(data)
            return
            
        itr = self.head

        while itr.next:                 # looping through the linked list to reach the second last element so that next elem points to None 
            itr = itr.next

        itr.next = Node(data, None)
        print(f'Inserted {data} at the end')

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at_index(self, data, index):
        if index<0 or index>self.get_length():
            print('Exception occured : index is not within range')
            return

        if index == 0:
            self.insert_at_beginning(data)
            return

        cnt = 0                         # need to iterate through the linked list in order to insert at
        itr = self.head

        while itr:
            if cnt == index - 1:
                itr.next = Node(data, itr.next)
                print(f'Inserted {data} at index {index}')
                break

            cnt += 1
            itr = itr.next

    def insert_ater_value(self, after_data, actual_data):
        itr = self.head
        flag = False

        while itr:                          # if list has got no node initially, then self.head is None, hence itr will be None, and while loop wont run
            if itr.data == after_data:
                itr.next = Node(actual_data, itr.next)
                print(f'Inserted {actual_data} after {after_data}')
                flag = True
                break

            itr = itr.next
        if flag == False:
            print(f'Could not find the node {after_data}')

    def remove_at(self, index):
        if self.head is None:
            print(f'Could not remove the node at index {index}')
            return

        if index<0 or index>self.get_length():
            print(f'Index {index} is outside range')
            return

        if index == 0:
            self.head = self.head.next
            print(f'Removed node at index {index}')
            return

        itr = self.head
        cnt = 0

        while itr:
            if cnt == index-1:
                itr.next = itr.next.next
                print(f'Removed node at index {index}')
                break
            itr = itr.next

    def remove_by_value(self, after_data):
        if self.head is None:
            print('Can not remove node')
            return

        if self.head.data == after_data:
            self.head = self.head.next
            print(f'Removed node {after_data}')
            return

        itr = self.head
        flag = False
        while itr.next:
            if itr.next.data == after_data:
                itr.next = itr.next.next
                flag = True
                print(f'Removed node {after_data}')
                break
            itr = itr.next

        if flag == False:
            print(f'Could not remove any node {after_data}')

if __name__ == '__main__':
    ll = LinkedList()

    # # # Insert functions
    print('Length of the linked list:', ll.get_length())
    ll.insert_at_beginning(12)
    print('Linked List :', ll)
    ll.insert_at_beginning(13)
    print('Linked List :', ll)
    ll.insert_at_end(11231)
    print('Linked List :', ll)
    ll.insert_at_end(100)
    print('Linked List :', ll)
    ll.insert_at_end(100)
    print('Linked List :', ll)
    ll.insert_at_index(4, 0)
    print('Linked List :', ll)
    ll.insert_at_index(8, 3)
    print('Linked List :', ll)
    ll.insert_ater_value(100, 22)
    print('Linked List :', ll)
    print('Length of the linked list:', ll.get_length())

    # # # Remove functions
    ll.remove_at(1)
    print('Linked List :', ll)
    ll.remove_by_value(11231)
    print('Linked List :', ll)





################## OUTPUT #####################

