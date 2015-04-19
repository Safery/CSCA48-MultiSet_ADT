from multiset_nodes import *
import random

class SkipList(object):
    '''A SkipList class using different types of Nodes and SingleLinkedList'''
    
    def __init__(self):
        '''(SkipList) -> NoneType
        Initialize a new SkipList
        '''
        self.cargo = SingleLinkedList()
    
    def insert(self, obj):
        '''(SkipList, Object) -> NoneType
        Inserts an object into the SkipList ADT
        '''
        self.obj = obj
        if (self.cargo.next_obj == None):
            new_obj = self.obj
            pass 
