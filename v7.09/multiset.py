from skiplist import *


class MultiSet():
    '''MultiSet class using the SkipList class'''

    def __init__(self):
        '''(MultiSet) -> NoneType
        Initialize a new MultiSet list by using/ implementing SkipList.
        '''
        self.skiplist = SkipList()

    def __contains__(self, item):
        '''(MultiSet, Elements) -> bool
        Returns True iff the elements belongs in the multiset.
        '''
        return self.skiplist.data.search(item)[0]

    def count(self, item):
        '''(MultiSet, Elements) -> int
        Returns the number of occurrences of elements in the multiset.
        '''
        return self.skiplist.data.search(item)[1]

    def insert(self, item):
        '''(MultiSet, Elements) -> NoneType
        Adds an elements to the multiset.
        '''
        # Inserts the item into the SkipList ADT implemented by self.skiplist
        self.skiplist.insert(item)

    def remove(self, item=None):
        '''(MultiSet, Elements) -> NoneType
        Removes one occurrence of an elements from the multiset.
        Ignores if elements is null
        '''
        # Returns None if no item was specified to remove.
        if (item == None):
            return None
        else:
            return self.skiplist.data.remove(item)


    def clear(self):
        '''(MultiSet) -> NoneType
        Clears all the elements from the multiset.
        '''
        # Clears the SkipList ADT.
        self.skiplist.data._clear()

    def __len__(self):
        '''(MultiSet) -> NoneType
        Returns the number of elements in Multiset.
        '''
        # Returns the actual length.
        return self.skiplist.data._len()

    def __repr__(self):
        '''(MultiSet, MultiSet) -> str
        Returns the string representation of the multiset.
        '''
        # If SkipList has objects else, return a empty repr.
        if (self.skiplist.data._len() > 0):
            # Empty str to be used for final return
            item = ''
            # Start at the first Node from the ADT.
            current = self.skiplist.data.head
            # Add it to the string
            item += str(current.data)
            current = current.next_node
            # Loop thought all the node until the tail Node.
            while current is not None:
                # Seperate the str representation of each obj
                item += ', '
                item += str(current.data)
                current = current.next_node
            # Returns the final str and the repr of the ADT.
            return 'MultiSet([' + item + '])'
        else:
            return 'MultiSet([])'

    def __eq__(self, multi_set):
        '''(MultiSet, MultiSet) -> bool
        Returns True iff multiset is exactly same as the given MultiSet
        '''
        # Check if they are both the same length
        if (len(self) == len(multi_set)):
            # Check if the repr are the same/ compare it. Returns True if True.
            if (self.__repr__() == multi_set.__repr__()):
                return True
            else:
                return False
        else:
            return False

    def __le__(self, multi_set):
        '''(MultiSet, MultiSet) -> bool
        returns True iff every element in MultiSet belongs to given MultiSet.
        '''
        # variable to determine if the found elements are same size as self.
        _x = 0
        # Determine and only continue iff the self size is <= given MultiSet
        if (len(self) <= len(multi_set)):
            # Start at the first Node from both MultiSet.
            current = self.skiplist.data.head
            current_multi = multi_set.skiplist.data.head
            # Loop thought all the element in given MultiSet.
            while (current is not None) and (current_multi is not None):
                # Adds to the var iff self has element in given MultiSet.
                if (str(current) == str(current_multi)):
                    _x += 1
                    # Change the current to next Node on both MultiSet
                    current = current.next_node
                    current_multi = current_multi.next_node
                else:
                    current_multi = current_multi.next_node
            # Return True iff all the element were in given MultiSet.
            # Determined if the _x has the same number as the length of self.
            if (_x == self.__len__()):
                return True
            else:
                return False
        else:
            return False

    def __sub__(self, multi_set):
        '''(MultiSet, MultiSet) -> MultiSet
        Returns a new multiset that contains every elements not from the given
        MultiSet but includes from the Original MulitSet. But the elements from
        Original MultiSet must not be in the given MultiSet.
        '''
        self.new_multi = MultiSet()
        # Select the head Node from the current MultiSet. 
        current_original = self.skiplist.data.head
        # Loops thought all the element in the original list
        while (current_original is not None):
            # Determine if the current element is in the Given MultiSet
            if(current_original.data in multi_set):
                current_original = current_original.next_node                
            else:
                # If not than insert it to the new MultiSet
                self.new_multi.insert(current_original.data)
                current_original = current_original.next_node
        # Return the new MultiSet
        return self.new_multi

    def __isub__(self, multi_set):
        '''(MultiSet, MultiSet) -> MultiSet
        Update the original MultiSet so that every elements from the given
        multiset is removed from the original.
        '''
        if (self == multi_set):
            self.clear()
        # Select the head Node from the current MultiSet. 
        current_original = self.skiplist.data.head
        # Loops thought all the element in the original list
        while (current_original is not None):
            # Determine if the current element is in the Given MultiSet
            if(current_original.data in multi_set):
                # Removes that element.
                self.remove(str(current_original.data))
                current_original = current_original.next_node                
            else:
                # If not than moves over to the next element.
                current_original = current_original.next_node
        return self

    def __add__(self, multi_set):
        '''(MultiSet, MultiSet) -> MultiSet
        Returns a new MultiSet that contains same element from the original
        and the given MultiSet.
        '''
        # Initialize a new MultiSet
        self.new_set = MultiSet()
        # Select the new first Node from both of the MultiSet
        current_head = self.skiplist.data.head
        current_multi_head = multi_set.skiplist.data.head
        # Loop thought the end of all longest/ both MultiSet
        while ((current_multi_head is not None) or (current_head is not None)):
            # Checks if one of the MultiSet has run out of Nodes.
            if ((current_multi_head is None) or (current_head is None)):
                # Returns the current MultiSet.
                return self.new_set
            # Checks the common/ Union of both element from the two MultiSet
            elif (str(current_multi_head.data) == str(current_head.data)):
                # If they are same, insert it to the new MultiSet
                self.new_set.insert(str(current_multi_head.data))
                current_multi_head = current_multi_head.next_node
                current_head = current_head.next_node
            else:
                # Go over to the next Node
                current_multi_head = current_multi_head.next_node
                current_head = current_head.next_node
        # Return the final/ newly modified MultiList
        return self.new_set

    def __iadd__(self, multi_set):
        '''(MultiSet, MultiSet) -> MultiSet
        Updates the original multiset so that it contains only elements that
        are common to both the original and the given MultiSet.
        '''
        # If the length of the given MultiSet is 0, return self MutliSet.
        if (len(multi_set) == 0):
            return self
        else:
            # Select the First Node from the given MultiSet
            current_multi_set = multi_set.skiplist.data.head
            # Loop thought all the Node of the MultiSet
            while (current_multi_set is not None):
                # Insert each each element from the given to the self MultiSet
                self.insert(str(current_multi_set.data))
                current_multi_set = current_multi_set.next_node
            # Return the newly modified self MultiSet
            return self

    def isdisjoint(self, multi_set):
        '''(self, MultiSet) -> bool
        Returns True iff the original MultiSet have no common elements as the
        given multiset.
        '''
        # selects the first Node from the given MultiSet
        current_multi_set = multi_set.skiplist.data.head
        # Loops throught all the Node and determine if self is holding it.
        while (current_multi_set is not None):
            # If a similiar Node is found on both MultiSet then return False.
            if (str(current_multi_set.data) in self):
                return False
            else:
                # Go to the next Node, iff self do not have the current Node
                current_multi_set = current_multi_set.next_node
        # Return True iff no same Node are found on both MultiSet
        return True

    def __and__(self, multi_set):
        '''(MultiSet, MultiSet) -> MultiSet
        Returns a new MultiSet that contains every element from the original
        and the given MultiSet.
        '''
        # Initialize a new MultiSet
        self.new_set = MultiSet()
        # Select the new first Node from both of the MultiSet
        current_head = self.skiplist.data.head
        current_multi_head = multi_set.skiplist.data.head
        # Loop thought the end of all longest/ both MultiSet
        while ((current_multi_head is not None) or (current_head is not None)):
            # If self is currently None, only insert Node from the other set.
            if ((current_multi_head is None) and (current_head is not None)):
                self.new_set.insert(str(current_head.data))
                # select the next Node from the self MultiSet
                current_head = current_head.next_node
                # If given set is Empty, insert element from the self MultiSet
            elif ((current_head is None) and (current_multi_head is not None)):
                self.new_set.insert(str(current_multi_head.data))
                # Select the next Node from the given MultiSet
                current_multi_head = current_multi_head.next_node
            else:
                # If they both have element, insert both Node to the new Set.
                self.new_set.insert(str(current_multi_head.data))
                self.new_set.insert(str(current_head.data))
                # Select the next Node from both of the MultiSet8
                current_head = current_head.next_node
                current_multi_head = current_multi_head.next_node
        return self.new_set

    def __iand__(self, multi_set):
        '''(MultiSet, MultiSet) -> MultiSet
        Returns a modified self MultiSet that contains every element from the
        original and the given MultiSet.
        '''
        pass


if __name__ == '__main__':
    x = MultiSet()
    x.insert(1)
    x.insert(2)
    x.insert(3)
    y = MultiSet()
    z = x + y

