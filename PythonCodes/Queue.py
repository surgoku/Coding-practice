'''
Created on Nov 27, 2016

@author: root
'''


class Queue:
    def __init__(self):
        self.items = []
    
    def pop(self):
        return self.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def peek(self):
        return self.items[0]
        
    
        
        