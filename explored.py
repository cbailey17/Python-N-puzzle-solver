'''

@author: mroch
'''
class Explored(object):
    "Maintain an explored set.  Assumes that states are hashable"

    def __init__(self):
        "__init__() - Create an empty explored set"
        #explored set will be dictionary data structure
        self.exploredSet = dict()
        
        
    def exists(self, state):
        """exists(state) - Has this state already been explored?
        Returns True or False, state must be hashable
        """
        #hash the state and find the key
        key = hash(state)
        if self.exploredSet.get(key):
            return True
        else:
            return False
        
    
    def add(self, state):
        """add(state) - add given state to the explored set.  
        state must be hashable and we asssume that it is not already in set
        """
        #bucket list for collisions
        bucket = []
        #hash the state and find the key
        key = hash(state)
        #add the key and state to the explored state
        if key in self.exploredSet.keys() == True :
            bucket.append({key: state})
            
        self.exploredSet.update({key : state})
     
        # The hash function is a Python builtin that generates
        # a hash value from its argument.  Use this to create
        # a dictionary key.  Handle collisions by storing 
        # states that hash to the same key in a bucket list.
        # Note that when you access a Python dictionary by a
        # non existant key, it throws a KeyError


            
