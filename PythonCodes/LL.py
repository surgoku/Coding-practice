'''
Created on Oct 16, 2016

@author: root
'''

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next 



def createList():
    elements = [10,7,11,0,3,5]
    root = Node(15)
    temp_node = root
    counter=0
    for i in elements:
        node = Node(i)
        temp_node.next = node
        
        counter+=1
        if counter <= len(elements)-1:
            temp_node = temp_node.next

    return root 


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
    root = createList()
    #print root.val
    while not root.next is None:
        print root.val
        root = root.next

    
    
run()