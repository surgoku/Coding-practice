'''
Created on Oct 28, 2016

@author: root
'''

class Node:
    val, left, right = None, None, None
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


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


def findDeepestCommonAncestorBT(root, a, b):
    ap1 = ap2 = ap3 = bp1 = bp2 = bp3 = None
    # parents to left
    if root.left:
        ap1, bp1 = findDeepestCommonAncestorBT(root.left, a, b)
    # parents to right
    if root.right:
        ap2, bp2 = findDeepestCommonAncestorBT(root.right, a, b)
    # are we an immediate "parent" ourselves?
    if root.val == a: 
        ap3 = root
    elif root.val == b:
        bp3 = root
    # only one of the above can succeed, so find it
    ap = ap1 or ap2 or ap3
    bp = bp1 or bp2 or bp3
    # if we are the point where two paths meet at the common
    # ancestor, return ourselves
    if ap and bp and ap != bp:
        return root, root
    # otherwise, return what we have
    else:
        return ap, bp
    
def main():
    
    #print 
    root = Node(5)
    root.left = Node(12)
    root.right = Node(1)
    root.left.left = Node(4)
    root.left.right = Node(50)
    root.right.left = Node(-6)
    root.right.right = Node(70)
    
    out_l, out_r =  findDeepestCommonAncestorBT(root,12,1)
    
    print out_l.val, out_r.val
        
            
main()