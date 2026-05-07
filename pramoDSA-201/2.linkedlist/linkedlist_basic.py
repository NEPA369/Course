# 1. Write a program to show the implementation of Linked List in python.  
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class LinkList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        # Encapsulating in node class
        node = Node(data)
        if self.head is None:
            self.head = node    
        else: 
            current = self.head 
            while current.next:
                current = current.next 
            current.next = node 
            
if __name__ == "__main__":           
    words = LinkList()
    words.append('Data')
    words.append('Science')
    words.append('Lab')
    
    current = words.head
    while current:
        print(current.data)
        current = current.next
