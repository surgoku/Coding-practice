'''
Created on Oct 16, 2016

@author: root
'''

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next 



def createList():
    node = Node(10)
    node = Node(7, node)
    node = Node(11, node)
    node = Node(0, node)
    node = Node(3, node)
    
    return node 


def containsLoop(root):
    slow = root
    fast = root
    
    while fast.next != None:
        slow = slow.next
        
        if fast.next !=None:
            fast = fast.next.next
            
        if fast is slow:
            return True
        
    return False

def run():
    node = createList()

    
    
run()