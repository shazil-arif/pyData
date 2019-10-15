from ds.Node import Node
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
        self.insert_helper(self.root, newVal)

    '''
    @param $value
        type: any (generally the binary search tree will hold values of one type but is not restricted to do so)
        (required) - the value to search in the binary search tree

    @return bool
        returns True if $value is found in the binary search tree
        returns False is $value is not found in the binary search tree
    '''
    def search(self,value):
        self.search_helper()

    '''
    @function insert_helper
        helper function to insert a new node into the binary search tree
        free client of hassle to pass in root node
        called from insert function
        
    '''
    @staticmethod
    def insert_helper(self, root, newVal):
        if (newVal <= root):
            if (self.left):
                self.insert_helper(self.left, newVal)
                #if the left node is defined, then compare newVal to that left node
                #call recursively where self.left becomes the "root"
            else:
                #if no left node is defined, then the left node itself
                #becomes the Node with newVal given
                self.left = Node(newVal)
        else:
            #repeat same process for values greater than the root,
            #to be inserted to the right of the tree
            if self.right:
                self.insert_helper(self.right,newVal)
            else:
                self.right = Node(newVal)


    @staticmethod 
    def search_helper(self, root, value):
        if(value == root):
            return True

        elif(value < root):
            #if value is less than root, then compare to the left node
            if (self.left):

                #call search_helper() recursively 
                #self.left becomes the 'root' at each recursive call

                return search_helper(self.root,value)

            else:
                #if the left node is of type None, i.e not assigned yet
                #then the value is most definitely not in the tree

                return False
        else:
            #repeat the same for the right side of the search tree
            if self.right:
                return search_helper(self.root,value)
            else:
                return False

