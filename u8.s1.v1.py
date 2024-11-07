
# Problem 1 Build a Binary Tree
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

rightNode = TreeNode(6)
leftNode = TreeNode(4)
root = TreeNode(10)

root.left = leftNode
root.right = rightNode

# Problem 2: 3-Node Sum 1
def check_tree(root):
    if (root.left.val + root.right.val) == root.val:
        return True
    else:
        return False

print(check_tree(root))



# Problem 3: 3-Node Sum 2
def check_tree2(root):
    if root.left and root.right:
        if (root.left.val + root.right.val) == root.val:
            return True
        else:
            return False
    else:
        return False

print(check_tree2(root))

print("______________")
# Problem 4: Find the Leftmost Node 1
def left_most(root):
    if not root:
        return None
    if not root.left:
        return root.val
    left_most(root.left)
    

print(left_most(root))
