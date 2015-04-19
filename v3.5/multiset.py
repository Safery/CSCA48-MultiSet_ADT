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
        pass
    
    def count(self, item):
        '''(MultiSet, Elements) -> int
        Returns the number of occurrences of elements in the multiset.
        '''
        pass
    
    def insert(self, item):
        '''(MultiSet, Elements) -> NoneType
        Adds an elements to the multiset.
        '''
        self.skiplist.insert(item)
        
    def remove(self, item=None):
        '''(MultiSet, Elements) -> NoneType
        Removes one occurrence of an elements from the multiset. Ignores if elements is null
        '''
        pass
    
    def clear(self):
        '''(MultiSet) -> NoneType
        Clears all the elements from the multiset.
        '''
        self.skiplist.data.head.next_node = self.skiplist.data.tail
    
    def __len__(self):
        '''(MultiSet) -> NoneType
        Returns the number of elements in Multiset.
        '''
        # Returns the actual length (minus 1 for excluding the NoneType head).
        return self.skiplist.data._len() - 1
    
    def __repr__(self):
        '''(MultiSet, MultiSet) -> str
        Returns the string representation of the multiset.
        '''
        
        if (self.skiplist.data._len() > 1):
            
            item = ''
            current = self.skiplist.data.head.next_node
            item += str(current.data)
            current = current.next_node
            while current != None:
                item += ', '            
                item += str(current.data)
                current = current.next_node
            return 'MultiSet([' + item + '])'
        else:
            return 'MultiSet([])'
    
    def __eq__(self, multi_set):
        '''(MultiSet, MultiSet) -> bool
        Returns True iff multiset is exactly same as the given MultiSet
        '''
        _x = 0
        if (self.skiplist.data._len() == multi_set.skiplist.data._len()):
            current = self.skiplist.data.head.next_node
            current_multi = multi_set.skiplist.data.head.next_node
            
            while (current != None) and (current_multi != None):
                if (current.data == current_multi.data):
                    current = current.next_node
                    current_multi = current_multi.next_node
                    _x += 1
                    
                else:
                    return False

            if (_x == self.skiplist.data._len()-1):
                return True
        else:
            return False

        
    
    def __le__(self, multi_set):
        '''(MultiSet, MultiSet) -> bool
        returns True iff every element in MultiSet belongs to given MultiSet.
        '''
        pass
    
    def __sub__(self, multi_set):
        '''(MultiSet, MultiSet) -> MultiSet
        Returns a new multiset that contains every elements not from the given MultiSet but includes from the Original.
        '''
        pass
    
    def __isub__(self, multi_set):
        '''(MultiSet, MultiSet) -> NoneType
        Update the original MultiSet so that every elements from the given multiset is removed from the original.
        '''
        pass
    
    def __add__(self, multi_set):
        '''(MultiSet, MultiSet) -> MultiSet
        Returns a new MultiSet that contains every element from the original and the given MultiSet.
        '''
        pass
    
    def __iand__(self, multi_set):
        '''(MultiSet, MultiSet) -> NoneType
        Updates the original multiset so that it contains only elements that are common to both the original and the given MultiSet.
        '''
        pass
    
    def isdisjoint(self, multi_set):
        '''(self, MultiSet) -> bool
        Returns True iff the original MultiSet have no common elements as the given multiset.
        '''
        pass
    
if __name__ == '__main__':
    x = MultiSet()
    x.insert(3)
    x.insert(2)
    x.insert(234)
    x.insert(1)
    y = MultiSet()
    x.clear()

    
