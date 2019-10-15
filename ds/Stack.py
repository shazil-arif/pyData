from LinkedList import LinkedList
class Stack:
    #stack implementation using a linked list
    def __init__(self,top=None):
        self.items = LinkedList(top)
    def pop(self):
        return self.items.deleteFirst()
    
    def push(self,newElement):
        self.items.insertFirst(newElement)

    def peek(self):
        return self.items.head
