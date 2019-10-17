'''
A class used to implement a min heap data structure using a list
'''
class Heap:
    def __init__(self):
        self.items = []

    '''
    pop removes the first element and returns it
    throw a index error if heap is empty for now
    '''
    def pop(self):
        if len(self.items)!=0:
            self.__heapifyDown()
            return self.items.pop(0)
        else:
            return IndexError

    '''
    return the first value in the heap
    throw index error if heap is empty for now
    '''

    def peek(self):
        if len(self.items)!=0:
            return self.items[0]
        else:
            return IndexError

    '''
    @param
        type: any
        (required) - the value to insert into the heap
    '''
    def push(self,value):
        self.items.append(value)
        self.__heapifyUp()
        
    '''
    as long as there is a parent whose value is greater than our newly inserted value then
    keep going up

    begin from end of array, new values are inserted at the end of the tree

    Then in the while loop:

        keep going as long as there is a parent node
        and value of parent is greater than newly inserted value
        because this means our current child is not in the right place

        if both are true, then swap those two nodes

        after swapping, the value at index has changed

        index no longer contains our newly inserted node

        the value at 'index' is now the parent of the newly inserted node

        we re assign index to be the parentindex of 'index'

        since 'index' is now the original parent

        index now has the originally/newly inserted node

        and we begin going up again starting from there
    '''

    def __heapifyUp(self):
        childIndex = len(self.items) - 1
        while(self.__hasParent(childIndex) and self.__getParentValue(childIndex) > self.items[childIndex]):
            self.__swap(childIndex,self.getParentIndex(childIndex))
            childIndex = self.getParentIndex(childIndex)

    '''
    element have to decrease down the heap
    when heapifying down we can't simplify swap the current parent with any child
    '''

    def __heapifyDown(self):
        parentIndex = 0
        while(self.hasLeftChild(parentIndex)):
            
            smallerChildIndex = self.getLeftChildIndex(parentIndex)

            if(self.hasRightChild(parentIndex)
             and self.getRightChildValue(parentIndex) < self.getLeftChildValue(parentIndex)):
                smallerChildIndex = self.getRightChildIndex(parentIndex)
            
            if items[parentIndex] < items[smallerChildIndex]:
                break

            else:
                self.__swap(parentIndex,smallerChildIndex)
            
            parentIndex = smallerChildIndex
             
    '''
    How to verify if a value at a given index has a parent?

        get its parent index
        if the index is within the bounds of the array then it is in the tree

    '''
    def hasParent(self, childIndex): return self.getParentIndex(childIndex) < len(self.items)

    def hasRightChild(self,parentIndex): return self.getRightChildIndex(parentIndex) < len(self.items)

    def hasLeftChild(self,parentIndex): return self.getLeftChildIndex(parentIndex) < len(self.items)

    def getParentValue(self, childIndex): return self.items[self.getParentIndex(childIndex)]
        
    def getLeftChildValue(self,parentIndex): return self.items[self.getLeftChildIndex(parentIndex)]

    def getRightChildValue(self,parentIndex): return self.items[self.getRightChildIndex(parentIndex)]

    def getParentIndex(self,childIndex): return childIndex/2 - 1 #will a odd number/2 be rounded up by .5 or down by .5?

    def getLeftChildIndex(self,parentIndex): return parentIndex*2 + 1

    def getRightChildIndex(self,parentIndex): return parentIndex*2 + 2
        
    '''
    function to swap two values in the heap
        - not exposed to client to maintain integrity of heap
    '''
    def __swap(self, indexOne, indexTwo):
        temp = self.items[indexTwo]
        self.items[indexTwo] = self.items[indexOne]
        self.items[indexOne] = temp

    def print(self): 
        for i in self.items: print(i)
    

def main():
    #for testing only    
    l = Heap()
    l.push(5)
    l.push(4)
    l.push(9)
    l.push(22)
    x = l.pop()
    l.print()
    
    
    #works so far!
main()

