import sys
sys.path.insert(1,'./ds')
from ds.Node import Node 
from ds.BinarySearchTree import BinarySearchTree

e1 = Node(1)

bst = BinarySearchTree(e1)
bst.insert(2)
bst.insert(3) #remember to insert values, not nodes!
bst.printInOrder()
