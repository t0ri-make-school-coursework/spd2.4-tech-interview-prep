# Given a singly-linked list, find the middle value in the list.
class LinkedListNode: 
    def __init__(self, data):
        self.data = data
        self.next = None
  
class LinkedList: 
    def __init__(self):
        self.head = None

    def prepend(self, new_node): 
        node = LinkedListNode(new_node)
        node.next = self.head
        self.head = node

    
    def total_nodes(self):
        count = 1
        node = self.head

        while node.next is not None:
            node = node.next
            count += 1

        return count
    
    
    def middle_value(self):
        mid = self.total_nodes() / 2
        node = self.head
        while node.next is not None and mid is not 0:
            node = node.next
            mid -=1

        return node.data


llist = LinkedList()
llist.prepend(1)
llist.prepend(2)
llist.prepend(3)
llist.prepend(4)
llist.prepend(5)
llist.prepend(6)
llist.prepend(1)
llist.prepend(2)
llist.prepend(3)
llist.prepend(4)
llist.prepend(5)
llist.prepend(6)
print(llist.total_nodes())
print(llist.middle_value())