'''
Created on Nov 27, 2016

@author: root
'''
class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    

class Queue(object):
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        if(not self.isEmpty()):
            return  self.items.pop()
    def isEmpty(self):
        return  self.items==[]
    def size(self):
        return len(self.items)



class stackUsingQueue(object):
        def __init__(self):
            self.q1= Queue()


        def push(self, item):
            self.q1.enqueue(item) 


        def pop(self):
            c=self.q1.size()
            while(c>1):
                self.q1.enqueue(self.q1.dequeue())
                c-=1
            return self.q1.dequeue()

        def size(self):
            return self.q1.size() 


        def isempty(self):
            if self.size > 0:
                return True
            else:
                return False