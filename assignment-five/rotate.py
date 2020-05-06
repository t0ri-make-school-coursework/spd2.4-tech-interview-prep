# Rotate a given singly-linked list counter-clockwise by k nodes, where k is a given integer.


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

  
    def rotate_by_k(self, k):
        node = self.head 
        count = 1 
        
        while count < k and node is not None:
            node = node.next
            count += 1

        last = node  
      
        while node.next is not None: 
            node = node.next
  
        node.next = self.head
        self.head = last.next
        last.next = None
  
  
llist = LinkedList() 
llist.prepend(1)
llist.prepend(2)
llist.prepend(3)
llist.prepend(4)
llist.prepend(5)
llist.prepend(6)
llist.rotate_by_k(4)