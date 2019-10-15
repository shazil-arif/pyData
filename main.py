import sys
sys.path.insert(1,'./ds')
from LinkedList import LinkedList
from Element import Element 
from Stack import Stack

linkedlist = LinkedList()
stack = Stack()

for i in range(10):
    e = Element(i+1)
    stack.push(e)

for i in range(10):
    print(stack.ll.getElement(i).value)

stack.pop()
print("-----")
for i in range(10):
    print(stack.ll.getElement(i).value)
    



# size = linkedlist.size()
# for i in range(size):
#     print(linkedlist.getElement(i).value)

# linkedlist.reverse()
# for i in range(size):
#     print(linkedlist.getElement(i).value)





