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


def findMaxWidthupdatedPostOrder(root, width):

    if not root:
        return 0
    
    if not root.left and not root.right:
        return 1
    
    temp_max_width = 0
    
    left_width = findMaxWidthupdatedPostOrder(root.left, width)  # 0 for 35
    right_width = findMaxWidthupdatedPostOrder(root.right, width)  # 1 for 36
    
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
    
    
def generateTreeFromPreOrderInOrderListsRecur(inorder, preorder):
    #given tree:
    #  4
    # 2  5
    #1 3 6 7
    # idea is to recursively build tree. Root is the first elem of pre-order
    # then iterate over inorder till root elemn left of this elem is left subtree and right
    # is right subtree. The root of 
    if not preorder:
        return
    root = preorder[0]
    tree = Node(root)
    if len(preorder) <= 1:
        return tree
    
    for i in range(len(inorder)):
        if inorder[i] == root:
            left_child = generateTreeFromPreOrderInOrderListsRecur(inorder[:i], preorder[1:i+1])
            right_child = generateTreeFromPreOrderInOrderListsRecur(inorder[i+1:], preorder[i+1:])
            tree.left = left_child
            tree.right = right_child
            
    return tree
    
def inorderTraversal(root):
    if not root:
        return
    if root.left:
        inorderTraversal(root.left)
    print root.val
    if root.right:
        inorderTraversal(root.right)
        
def generateTreeFromPreOrderInOrderLists():
    #given tree:
    #  4
    # 2  5
    #1 3 6 7
    inorder = [1,2,3,4,6,5,7]
    preorder = [4,2,1,3,5,6,7]
    
    tree = generateTreeFromPreOrderInOrderListsRecur(inorder, preorder)
    
    inorderTraversal(tree)


def findLeftRightMostWidths(root, minMax, dist):
    if not root:
        return
    
    if minMax[0] >= dist :
        minMax[0] -= 1
    
    if minMax[1] <= dist :
        minMax[1] += 1
        
    findLeftRightMostWidths(root.left, minMax, dist-1)
    findLeftRightMostWidths(root.left, minMax, dist+1)
        
        

def printVerticalHelper(root, curr_level, dist):
    if not root:
        return
    if dist == curr_level:
        print root.val
    
    printVerticalHelper(root.left, curr_level, dist-1)
    printVerticalHelper(root.right, curr_level, dist+1)
    

def printVertical(root):
    minMax = [0,0]
    dist = 0
    findLeftRightMostWidths(root, minMax, dist)
    
    for i in range(minMax[0], minMax[1]+1):
        printVerticalHelper(root, i, 0)
        print


def isCompleteBtree(root):
    #A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible. See following examples.
    if not root:
        return True
    
    queue = []
    queue.append(root)
    
    flag = False
    
    while len(queue) > 0:
        curr = queue.pop(0)
        
        if curr.left:
            if flag == True:
                return False
            
            queue.append(curr.left)
        else:
            flag = True
            
        if curr.right:
            if flag == True:
                return False
            
            queue.append(curr.right)
        else:
            flag = True
            
    
    return True
        
        
        


def main():
    
    #print 
    root = Node(5)
    root.left = Node(12)
    root.right = Node(1)
    root.left.left = Node(4)
    root.left.right = Node(50)
    root.right.left = Node(-6)
    root.right.right = Node(70)
    
    printVertical(root)

    
    out_l, out_r =  findDeepestCommonAncestorBT(root,12,1)
    
    #print out_l.val, out_r.val
    
    #generateTreeFromPreOrderInOrderLists()
        
            
main()