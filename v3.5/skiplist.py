import random

class Node():
    '''A node for skip list object'''

    def __init__(self, data, next_node=None, down=None):
        '''(Node, object, int, Node) -> NoneType
        Initialize a new Node with height and a linked to next Node.
        '''
        self.next_node = next_node
        self.data = data
        self.down = down

    def __str__(self):
        '''(Node) -> str
        Return the string representation the Node
        '''
        return str(self.data)

class HeadNode(Node):
    '''A head node for skip list object'''
    
    def __init__(self):
        Node.__init__(self, None, next_node=None, down=0)
        


class TailNode(Node):
    '''A tead node for skip list object'''

    def __init__(self):
        Node.__init__(self, None, next_node=None, down=0)

class SingleLinkedList(object):
    '''A Single linked list class using the Node class.'''
    
    def __init__(self, height=0):
        '''(SingleLinkedList) -> NoneType
        Initialize a new Single Linked List.
        '''
        self.head = HeadNode()
        self.tail = TailNode()
        self.height = None

    def __str__(self):
        '''(SingleLinkedList) -> str
        Return the string representation the single linked list.
        '''

        s = ''
        current = self.head
        while (current != None):
            s += str(current)
            current = current.next_node
        return s


    def insert(self, obj):
        '''(SingleLinkedList, object) -> NoneType
        Adds a object to the tail of the Single linked list.
        '''
        # Intialize a new Node object.
        new_node = Node(obj)
        # Check whether the list is empty or has data inside.
        if (self.head.data == None):
            # Adds the new Node object to the front of the list.
            self.head.data = new_node
        else:
            # holds the current data
            current = self.head
            # Loops until to the tail of the list
            while (current.next_node != None):
                current = current.next_node
            # Adds the given object to the tail of the list.
            current.next_node = new_node

    def _len(self):
        '''(SingleLinkedList) -> int
        Returns the length of the current list.
        '''
        if (self.head.data == None):
            return 0
        else:
            # holds the current position of the top list
            current = self.head
            i = 0
            # loops all the way to the end of the list
            while (current != None):
                current = current.next_node
                i += 1
            # Return the length of the list.
            return i

    def remove(self, obj):
        '''(SingleLinkedList, object) -> NoneType
        Removes the given object from the LinkedList. If not object
        specified, than it returns a NoneType.
        '''
        # Holds the current data from top of the list
        current = self.head
        # Gets the current length of the list, so while loop don't go infinite.
        get_len = self._len()
        _i = 0
        # Returns NoneType iff there are no given object in the list to remove.
        try:
        # Loop thought all the item until obj == current from the list.
            while (current.next_node.data != obj) and (_i <= get_len):
                current = current.next_node
                _i += 1
            # Gets the removed value to be used for the return
            return_val = current.next_node.data
            # Sets the previous Node link to the Node after the next Node
            current.next_node = current.next_node.next_node
            return return_val
        except:
            return None

class SkipList(object):
    '''A SkipList class using different types of Nodes and SingleLinkedList'''
    
    def __init__(self):
        '''(SkipList) -> NoneType
        Initialize a new SkipList
        '''
        self.data = SingleLinkedList()
        
    def __str__(self):
        '''(SkipList) -> str
        Return the string representation the SkipList.
        '''
        pass
        
    def _get_sort(self, sorting_list):
        '''(SkipList, [list of objects]) -> [lists of objects]
        Orders the set from least to greatest objects. Returns the sorted list.
        REQ: object must be sortable.
        '''
        # Loops thought all the objects from 0th element to the end.
        for objects in range(len(sorting_list)):
            # Gets the 0th element.
            get_val = sorting_list[objects]
            i = objects -1
            
            while i >= 0:
                # If the chosen element is smaller than its previous element.
                if (get_val < sorting_list[i]):
                    # Swithc the element from <.
                    sorting_list[i + 1] = sorting_list[i]
                    sorting_list[i] = get_val
                    i = i - 1
                # If previous element is smaller break the loop to next element. 
                else:
                    break
        return sorting_list

    
    def insert(self, obj):
        '''(SkipList, Object) -> NoneType
        Inserts an object into the SkipList ADT
        '''
        self.data.insert(obj)


        
if __name__ == '__main__':
    x = SkipList()
    x.insert(3)
    x.insert(2)
    print(x)
            
