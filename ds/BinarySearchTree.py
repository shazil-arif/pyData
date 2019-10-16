from .Node import Node
import sys
class BinarySearchTree:
    '''
    @param root
        type: Node
        (required) - the root node of the binary search tree
    '''
    def __init__(self, root):
        self.root = root
    
    '''
    @param $newVal
        type: any
        (required) - the value to insert into the binary search tree
    '''
    def insert(self,newVal):
        self.insertHelper(self.root, newVal)

    '''
    @function insert_helper
        helper function to insert a new node into the binary search tree
        free client of hassle to pass in root node
        called from insert function  
    '''
    @staticmethod
    def insertHelper(self, currentNode, newVal):
        #currentNode can be thought of as the 'root' at each recursive call
        if (newVal <= currentNode.value):
            if (currentNode.left):
                self.insertHelper(currentNode.left, newVal)
                #if the left node is defined, then compare newVal to that left node
                #call recursively where self.left becomes the "root" or currentNode
            else:
                #if no left node is defined, then the left node itself
                #becomes the Node with newVal given
                currentNode.left = Node(newVal)
        else:
            #repeat same process for values greater than the root,
            #to be inserted to the right of the tree
            if currentNode.right:
                self.insertHelper(currentNode.right,newVal)
            else:
                currentNode.right = Node(newVal)

    '''
    @param $value
        type: any (generally the binary search tree will hold values of one type but is not restricted to do so)
        (required) - the value to search in the binary search tree

    @return bool
        returns True if $value is found in the binary search tree
        returns False is $value is not found in the binary search tree
    '''
    def search(self,value):
        return self.searchHelper(self.root,value)

    '''
    @param $value
        type: any (generally, the the type is consistent across the BST but is not required to be)
        (required) - the value to delete from the BST
    '''
    def delete(self,value):
        pass


    '''
    @function insert_helper
        helper function to search for a given node in the binary search tree
        free client of hassle to pass in root node
        called from search function
    '''
    @staticmethod 
    def searchHelper(self, currentNode, value):
        root = currentNode.value
        if(value == root):
            return True

        elif(value < root):
            #if value is less than root (value of currentNode), then compare to the left node
            if (currentNode.left):

                #call search_helper() recursively 
                #self.left becomes the 'root' at each recursive call

                return self.searchHelper(currentNode.left,value)

            else:
                #if the left node is of type None, i.e not assigned yet
                #then the value is most definitely not in the tree

                return False
        else:
            #repeat the same for the right side of the search tree
            if currentNode.right:
                return self.searchHelper(currentNode.right,value)
            else:
                return False

    '''
    @param root
        type: Node
        (required) - The root/ top level Node of the BST to validate
    '''
    def isValidBST(self, root):
        return self.validBST(root,-sys.maxint-1,sys.maxint)

    '''
    helper function for validating a BST
    '''
    @staticmethod
    def validBST(self, currentNode, _min, _max):

        #currentNode can be thought of as the root node at 
        #each recursive call

        if (currentNode == None):
            return True
        if (currentNode.val < _min or currentNode.val > _max):
            return False

        #our upper bound max, will be the value of the node we just checked minus 1 when checking the left of the current node
        #the lower bound min, will be the value og the node we just checked plus 1 when checking the right of the current node

        return self.validBST(currentNode.left, _min, currentNode.val - 1) and self.validBST(currentNode.right, currentNode.val + 1, _max)

    
    def printPreOrder(self):
        self.printPreOrderHelper()

    '''
    helper function to print out nodes in BST, in a pre order manner 
    '''
    @staticmethod
    def printPreOrderHelper(self,node):
        if node:
            print(node.value)
            self.printPreOrder(node.left)
            self.printPreOrder(node.right)
