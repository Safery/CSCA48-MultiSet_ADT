import random


class Node():
    '''A node for skip list object'''

    def __init__(self, data, next_node=None, up_node=None, down_node=None):
        '''(Node, object, int, Node) -> NoneType
        Initialize a new Node with height and a linked to next Node.
        '''
        self.next_node = next_node
        self.data = data
        self.up_node = up_node
        self.down_node = down_node

    def __str__(self):
        '''(Node) -> str
        Return the string representation the Node
        '''
        return str(self.data)


class HeadNode(Node):
    '''A head node for skip list object'''

    def __init__(self):
        Node.__init__(self, None, next_node=None, up_node=None, down_node=None)


class TailNode(Node):
    '''A tead node for skip list object'''

    def __init__(self):
        Node.__init__(self, None, next_node=None, up_node=None, down_node=None)


class SingleLinkedList(object):
    '''A Single linked list class using the Node class.'''

    def __init__(self):
        '''(SingleLinkedList) -> NoneType
        Initialize a new Single Linked List.
        '''
        # Initialize both the HeadNode and the TailNode
        self.head = HeadNode()
        self.tail = TailNode()

    def __str__(self):
        '''(SingleLinkedList) -> str
        Return the string representation the single linked list.
        '''
        # temp var list to hold the objects for return
        _x = []
        # select the HeadNode
        current = self.head
        # Loop thought all the bottom Node from Left to Right.
        while (current is not None):
            # Select the up Node on the current Node.
            current_up = current
            # get the next node iff there is an up Node.
            while (current_up is not None):
                current_up_next = current_up
                s = 'head -> '
                # loop thought all the connected linked Node.
                while(current_up_next is not None):
                    # convert it to str and add it to the return str.
                    s += str(current_up_next)
                    s += ' -> '
                    # select the next Node
                    current_up_next = current_up_next.next_node
                s += 'tail'
                # add it to the temp list.
                _x.append(s)
                # select the next up Node
                current_up = current_up.up_node
                # select the next Node (from level 1)
            current = current.next_node
        # Reverse the list
        _x = _x[::-1]
        return_str = ''
        # loops thought all the reversed str and inserts it to the return str.
        for each in _x:
            return_str += each
            return_str += '\n'
        # returns the final str.
        return return_str

    def _clear(self):
        '''(SingleLinkedList) -> NoneType
        Clears the current SingleLinkedList
        '''
        # ReInitialize both the Node.
        self.head = HeadNode()
        self.tail = TailNode()

    def insert(self, obj):
        '''(SingleLinkedList, object) -> NoneType
        Adds a object to the tail of the Single linked list.
        '''
        # Check whether the list is empty or has data inside.
        if (self.head.data is None):
            # Intialize a new Node object.
            new_node = Node(obj)
            # Adds the new Node object to the front of the list.
            self.head.data = new_node
            # Randomly determine if a new Level needed to be placed.
            while (random.random() < 0.5):
                # Selects the first Node
                current = self.head
                # Moves to the top level (If there is one)
                while (current.up_node is not None):
                    current = current.up_node
                # Creates a new Node with the top being None and bottom prev.
                new_node = Node(obj, up_node=None, down_node=current)
                # Links the current Node with the newly created Node.
                current.up_node = new_node

        else:
            # Intialize a new Node object.
            new_node = Node(obj)
            # holds the current data
            current = self.head
            # Loops until to the tail of the list
            while (current.next_node is not None):
                current = current.next_node
            # Links the new Node to the end of the list.
            current.next_node = new_node
            current = current.next_node
            # Randomly determine if a new Level needed to be placed.
            while (random.random() < 0.5):
                # Loops to the top level of the selected Node (If there is one)
                while (current.up_node is not None):
                    current = current.up_node
                # Links the new Node to the bottom and places on the top level.
                new_node = Node(obj, up_node=None, down_node=current)
                current.up_node = new_node
            # Selects the first Node.
            current = self.head
            # loops to the 2nd last Node in the ADT.
            while (current.next_node.next_node is not None):
                current = current.next_node
            # Selects both the last and the 2nd last Node
            current_up_node_1 = current
            current_up_node_2 = current.next_node
            # Determines if both Node contains any Level.
            # Since the New Node was placed at the end ofthe list. Its upper
            # level Node needs to be connected with the prev level Nodes.
            if ((current_up_node_2.up_node is None) or
               (current_up_node_1.up_node is None)):
                pass
            else:
                # Loops thought all the level from the both selected Node
                while ((current_up_node_1.up_node is not None) and
                       (current_up_node_2.up_node is not None)):
                    # Links them together from both Node (to be used as a
                    # next_node on upper levels).
                    current_up_node_1.next_node = current_up_node_2.up_node
                    current_up_node_1 = current_up_node_1.up_node
                    current_up_node_2 = current_up_node_2.up_node

    def _len(self):
        '''(SingleLinkedList) -> int
        Returns the length of the current list.
        '''
        if (self.head.data is None):
            return 0
        else:
            # holds the current position of the top list.
            current = self.head
            i = 0
            # loops all the way to the end of the list.
            while (current is not None):
                current = current.next_node
                i += 1
            # Return the length of the list.
            return i

    def search(self, obj):
        '''(SingleLinkedList, object) -> NoneType
        Searches for the object in the SingleLinkedList. Returns True iff
        the object exists.
        '''
        # Variable to keep track of # of occurrence of the element
        _ocu = 0
        # Start the first Node for it to loop thought all the other Node
        current_org = self.head
        while(current_org is not None):
            # Goes to top of the Node level
            current = current_org
            while (current.up_node is not None):
                current = current.up_node
            # Selects the bottom Node
            current_down = current
            # Loops thought all the bottom Node that is connected with the top.
            while (current_down.down_node is not None):
                # Selects the next Node that is connected with the Bottom Node.
                current_next = current_down
                # Loops thought all the next Node that is connected.
                while (current_next.next_node is not None):
                    # adds occurrence of the obj is same as the Linked data.
                    if (current_next.data == str(obj)):
                        # Goes to next
                        current_next = current_next.next_node
                    else:
                        # Moves over to the next Node
                        current_next = current_next.next_node
                # Selects the bottom Node
                current_down = current_down.down_node
            # adds occurrence of the obj is same as the Linked data.
            if (str(current_org.data) == str(obj)):
                _ocu += 1
                current_org = current_org.next_node
            else:
                # Goes over to the next Node.
                current_org = current_org.next_node
        # Returns True/ # of occurrence iff there was any occurrences.
        if (_ocu > 0):
            return (True, _ocu)
        else:
            # Returns False, if the algorithm fails to find same element.
            return (False, _ocu)

    def remove(self, obj):
        '''(SingleLinkedList, object) -> NoneType
        Removes the given object from the LinkedList. If not object
        specified, than it returns a NoneType.
        '''
        # Start the first Node for it to loop thought all the other Node
        current_org = self.head
        if (str(current_org.data) == str(int(obj))):
            current_replacer = current_org.next_node
            self.head = current_replacer
            # Return the removed Node
            return obj
        else:
            while(current_org is not None):
                # Goes to top of the Node level
                current = current_org
                while (current.up_node is not None):
                    current = current.up_node
                # Selects the bottom Node
                current_down = current
                # Loops thought all the bottom Node that is connected with top.
                while (current_down.down_node is not None):
                    # Selects the next Node that is connected with Bottom Node.
                    current_next = current_down
                    # Loops thought all the next Node that is connected.
                    while (current_next.next_node is not None):
                        # True iff the given data is same as the Linked data.
                        if (current_next.data == str(obj)):
                            # disconnect the link (to remove)
                            current_replacer = current_next.next_node.next_node
                            current_next.next_node = current_replacer
                        else:
                            # Goes over to the next Node
                            current_next = current_next.next_node
                    # Goes to the bottom Node
                    current_down = current_down.down_node
                    # First checks if the current Node is same as the given obj
                    if (str(current_org.data) == str(obj)):
                        current_replacer = current_org.next_node
                        self.head = current_replacer
                        # Return the removed Node
                        return obj
                    # If the bottom Node link is connected with the given obj.
                if (str(current_org.next_node) == str(obj)):
                    # disconnect the link (to remove)
                    current_replacer = current_org.next_node.next_node
                    current_org.next_node = current_replacer
                    # Return the removed Node
                    return obj
                else:
                    # Goes over to the next bottom Node.
                    current_org = current_org.next_node

    def _return_list(self):
        '''(SingleLinkedList) -> list of int
        Returns the list of int from the current SingleLinkedList.
        '''
        _i = []
        # Choose the current Node
        current = self.head
        # Loop to the end
        while (current is not None):
            # Export all the data to the list
            _i.append(str(current))
            current = current.next_node
        # Return the final list.
        return _i


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
        # Return the str representation of the SkipList
        return str(self.data)

    def _get_sort(self, sorting_list):
        '''(SkipList, [list of objects]) -> [lists of objects]
        Orders the set from least to greatest objects. Returns the sorted list.
        REQ: object must be sortable.
        '''
        # Loops thought all the objects from 0th element to the end.
        for objects in range(len(sorting_list)):
            # Gets the 0th element.
            get_val = sorting_list[objects]
            i = objects - 1
            while i >= 0:
                # If the chosen element is smaller than its previous element.
                if (get_val < sorting_list[i]):
                    # Swithc the element from <.
                    sorting_list[i + 1] = sorting_list[i]
                    sorting_list[i] = get_val
                    i = i - 1
                # previous element is smaller break the loop to next element.
                else:
                    break
        return sorting_list

    def insert(self, obj):
        '''(SkipList, Object) -> NoneType
        Inserts an object into the SkipList ADT
        '''
        # If SingleLinkedList has no object, just insert without sorting
        if (self.data._len() == 0):
            # Checks if the obj is a Bool. To convert it to int if True.
            if (isinstance(obj, bool)):
                self.data.insert(int(obj))
            else:
                self.data.insert(obj)
        else:
            # Gets the return list of the current self.
            y = self.data._return_list()
            y.append(str(int(obj)))
            # All the elements gets sorted by Insertion method.
            x = self._get_sort(y)
            # clear the current SingleLinkedList
            self.data._clear()
            # Create a new SingleLinkedList with the sorted obj.
            for each_obj in x:
                self.data.insert(each_obj)

    def remove(self, obj):
        '''(SkipList, Object) -> NoneType
        Remove an Object from the SkipList ADT
        '''
        # Remove the object from the SkipList ADT.
        self.data.remove(obj)
