import copy

class Node:
    val, left, right = None, None, None
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class bst:
    root, size = None, 0
    
    def __init__(self, root=None):
        self.root = root
        self.size = 0
        
        
    def insert(self, root, data):

        if root is None:
            root = Node(data)
        
        elif data < root.val:
            if root.left is None:
                root.left = Node(data)
            else:  
                self.insert(root.left, data)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                self.insert(root.right, data)
            
        return
            
    
    def inOrder(self, root):
        #temp = copy.copy(root)
        if not root:
            return 
        
        self.inOrder(root.left)
        print root.val
        self.inOrder(root.right)
            
    

def createBST(tree):
    l = [5,1,3,6,1,2,7,8] # [1,1,2,3,5,6,7,8]
    mid_elem = sorted(l)[len(l)/2]
    # mid element can be selected in O(n) using quick select
    root = Node(mid_elem)
    tree.root = root
    for i in l:
        tree.insert(tree.root, i)
    
    return tree

def findLowestCommonAncestor(root, val1, val2):
    if val1 == val2:
        return False
    
    if root is None:
        return False
    
    if (root.val >= val1 and val2 > root.val) or (root.val >= val2 and val1 > root.val):
        return root.val
    
    else:
        return findLowestCommonAncestor(root.left, val1, val2) or findLowestCommonAncestor(root.right, val1, val2)
    
    
## This method gets the maximum width (span) of the bst
def updatedPostOrder(root, width):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    
    temp_max_width = 0
    
    left_width = updatedPostOrder(root.left, width)  # 0 for 35
    right_width = updatedPostOrder(root.right, width)  # 1 for 36
    
    temp_max_width = max(left_width, right_width)
    
    if width <  left_width + right_width + 1:
        width =  left_width + right_width + 1
    
    return  temp_max_width


def getKlargestElement(root):
    # do reverse-inorder traversal and have a counter. when counter is k that is the kth largest
    # or do in-order, pass in a list and then get n-k-1 element.
    pass

def main():
    tree = bst()
    tree = createBST(tree)
    #print tree.root.val
    #tree.inOrder(tree.root)
    
    #print 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    print findLowestCommonAncestor(tree.root,7,1)
        
            
main()
        
        
        