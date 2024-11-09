# Print binary tree
def printTree(node, level=0):
    if node is not None:
        printTree(node.right, level + 1)
        print( ' ' * 4 * level + '->' + str(node.value))
        printTree(node.left, level + 1)
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

rightNode = TreeNode(6)
leftNode = TreeNode(4)
root = TreeNode(10, leftNode, rightNode)

rNode1 = TreeNode(5)
lNode1 = TreeNode(3)
root1 = TreeNode(10, lNode1, rNode1)

rNode2 = TreeNode(5)
lNode2 = TreeNode(3)
root2 = TreeNode(10, lNode2)

rNode3 = TreeNode(10)
lNode3 = TreeNode(0)
root3= TreeNode(10, None, rNode3)


rlNode4 = TreeNode(3)
rNode4 = TreeNode(2, rlNode4, None)
root4 = TreeNode(1, None, rNode4)
'''
Visualization of tree above
     1
      \
       2
      / 
     3
'''

lrNode5 = TreeNode(3)
llNode5 = TreeNode(4)
rNode5 = TreeNode(5)
lNode5 = TreeNode(2, llNode5, lrNode5)
root5 = TreeNode(1, lNode5, rNode5)
'''
      1
     / \
    /   \
   2     5
  / \    
 4   3
'''

print("P1______________")
# Problem 1 Build a Binary Tree
print(f"root: {root.val}")
print(f"leftNode: {root.left.val}")
print(f"rightNode: {root.right.val}")



print("P2______________")
# Problem 2: 3-Node Sum 1

def check_tree(root):
    if root.left and root.right:
        if (root.left.val + root.right.val) == root.val:
            return True
        else:
            return False

print(f"True ?= {check_tree(root)}")
print(f"False ?= {check_tree(root1)}")



print("P3______________")


# Problem 3: 3-Node Sum 2
def check_tree2(root) -> int:
    sum:int = 0
    if root:
        if root.left or root.right:
            if root.left:
                sum = sum + root.left.val
            if root.right:
                sum = sum + root.right.val
        if root.val == sum:
            return True
    return False

print(check_tree2(root))
print(check_tree2(root2))
print(check_tree2(root3))

print("P4______________")
# Problem 4: Find the Leftmost Node 1
def left_most_recursive(root):
    if not root:
        return None
    if not root.left:
        return root.val
    return left_most_recursive(root.left)
    

print( left_most_recursive(root))
print( left_most_recursive(root2))
print( left_most_recursive(root3))


print("P5______________")
def left_most_iterative(root):
    while root:
        if root.left:
            root = root.left
            continue
        if not root.left:
            return root.val
    return None


print( left_most_iterative(root))
print( left_most_iterative(root2))
print( left_most_iterative(root3))



print("P6______________")
# Inorder is left, current, right
def inorder_traversal(root):
    lst = []

    def inorder_helper(node):
        if not node:
            return None
        if node.left:
            inorder_helper(node.left)
        lst.append(node.val)
        if node.right:
            inorder_helper(node.right)

    inorder_helper(root)

    return lst

print(inorder_traversal(root4))
print(inorder_traversal(root5))


print("____________p7")
def size(root):
    if not root:
        return 0
    return 1 + size(root.left) + size(root.right)

print(size(root5))

print("____________p8")
def find(root, value):
    if not root:
        return False
    if root.val == value:
        return True
    if value < root.val:
        find(root.left, value)
    else:
        find(root.right, value)

print(find(root5, 3))
