class LinkedList:
    '''
    @param $head
        (optional) - the node to set as the head of the linked list upon instantiation
    '''
    def __init__(self, head=None):
        self.head = head
    
    '''
    @param $new_element
        (required) - the node to be appended to the end of the linked list
        
        Type: an instance of the Element class found in this package
    '''

    def append(self, new_element):
        if not self.isEmpty():
            current = self.head
            while current.next:
                current = current.next
            current.next = new_element

        else:
            self.head = new_element

    '''
    @param $position
        (required) - Assuming the linked list count starts at 1 

        position is the 'index' of the node to get
    '''

    def getElement(self, position):
        #get an element a specific position, assuming elements are numbered starting from 1
        if not self.isEmpty():
            counter = 1
            current = self.head
            while current.next and counter < position:
                current = current.next
                counter += 1
            return current
        else:
            return

    def getLast(self):
        #get last node of linked list
        if not self.isEmpty():
            current = self.head
            while(current.next):
                current = current.next
            return current
        else:
            return self.throwEmptyWarning()

    '''
    @param $position
        (required) - the position to insert a new node at
        If 3 is passed as a parameter, then a new node will be inserted between position 2 and 3
    '''
    def insert(self,position,new_element):
        if not self.isEmpty():
            if position > 1:
                counter = 1
                current = self.head

                while(current and counter < position):
                    if (counter == position - 1):
                        new_element.next = current.next
                        current.next = new_element
                    current = current.next
                    counter += 1
                    
            elif position == 1:
                new_element.next = self.head
                self.head = new_element

            else:
                return self.throwTypeWarning()

        else:
            new_element.next = self.head
            self.head = new_element

    def insertFirst(self,new_element):
        '''insert a new element at the beginning of linked list'''
        if not self.isEmpty():
            try:
                new_element.next = self.head
                self.head = new_element
            except TypeError:
                return self.throwEmptyWarning()

        else:
            self.head = new_element

    '''
    @return int
        an integer representing the size of the linked list
    '''
    def size(self):
        '''get the size of the linked list'''
        if not self.isEmpty():
            count = 1
            current = self.head
            while current.next:
                current = current.next
                count += 1
            return count
        else:
            return 0

    def reverse(self):
        if not self.isEmpty():
            current = self.head
            previous = None
            while(current.next):
                next = current.next
                current.next = previous
                previous = current
                current = next
            self.head = previous

        else:
            return self.throwEmptyWarning()    
  
    '''
    @param $value
        (required) -  the value to be deleted from the linked list
    '''
    def delete(self, value):
        # delete the first instance of a value from linked list
        if not self.isEmpty():
            current = self.head
            previous = None
            while(current.value != value and current.next):
                previous = current
                current = current.next
                if (current.value == value):
                    if previous:
                        previous.next = current.next
                    else:
                        #if previous is of type None, then linked list is of size 1
                        #then point the head to current.next
                        self.head = current.next
        else:
            return self.throwEmptyWarning()

    '''
    @return node
        return the deleted node
    '''
    def deleteLast(self):
        if not self.isEmpty():
            current = self.head
            previous = None
            while(current.next):
                previous = current
                current = current.next
            deleted_element = current
            previous.next  = None
            return current

        else:
            return self.throwEmptyWarning()

    '''
    @return node
        return the deleted node
    '''
    def deleteFirst(self):
        if not self.isEmpty():
            deleted_el = self.head
            self.head = deleted_el.next
            return deleted_el

        else:
            return self.throwEmptyWarning()

    '''
    @return bool
        a boolean value
        True if the linked list is not empty
        False is it is empty
    '''
    def isEmpty(self):
        return self.head == None

    @staticmethod
    def throwEmptyWarning():
        return TypeError
        
    @staticmethod
    def throwTypeWarning():
        return TypeError
