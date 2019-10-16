'''
A class used to implement the heap data structure using a list
'''
class Heap:
    def __init__(self):
        self.items = []

    '''
    pop removes the first element and returns it
    '''
    def pop(self):
        if len(self.items)!=0:
            val = self.items[0]
            return self.items.pop(0)
        else:
            return IndexError

    '''
    @param
        type: any
        (required) - the value to insert into the heap
    '''
    def insert(self,value):
        self.items.append(value)
        

    def heapifyUp(self):
        pass

    def heapifyDown(self):
        pass
    
    def swap(self):
        pass

    def print(self):
        for i in self.items:
            print(i)


def main():
    #for testing only    
    l = Heap()
    l.insert(5)
    l.insert(4)
    l.insert(9)
    l.insert(22)
    x = l.pop()
    l.print()
main()

