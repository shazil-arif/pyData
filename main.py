import sys
sys.path.insert(1,'./ds')
from LinkedList import LinkedList
from Element import Element 

elements = []
for i in range(10):
    e = Element(i+1)
    elements.append(e)

linkedlist = LinkedList()
for i in elements:
    linkedlist.append(i)

size = linkedlist.size()
for i in range(size):
    print(linkedlist.getElement(i).value)

linkedlist.reverse()
for i in range(size):
    print(linkedlist.getElement(i).value)



