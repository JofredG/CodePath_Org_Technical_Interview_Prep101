"""
Print all the elements in a binary tree.
"""


class TreeNode:

  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

'''
Understand:
Input: root 
Output: print out individual nodes(any order)

Plan: recursively look through bst and print every node
left, root, right

edge case: 
root is none return None

time: O(n)
space: O(1)
'''

def printAllNodes(root):
  if not root:
    return None
  printAllNodes(root.left)
  print(root.val)
  printAllNodes(root.right)

node10 = TreeNode(10)
node20 = TreeNode(20)
node30 = TreeNode(30)
node35 = TreeNode(35)
node40 = TreeNode(40)
node50 = TreeNode(50)
node60 = TreeNode(60)
node65 = TreeNode(65)
node70 = TreeNode(70)
node80 = TreeNode(80)
node50.left = node30
node50.right = node70
node30.left = node20
node30.right = node40
node20.left = node10
node40.left = node35
node70.left = node60
node70.right = node80
node60.right = node65

printAllNodes(node50)

#Given a binary tree return the maxValue
#

def maxValue(root):
  currMax = -99999
  def traverse(node):
    nonlocal currMax
    if node.val > currMax:
      currMax = node.val
    traverse(root.left)
    traverse(root.right)
    return
  traverse(root)
  return currMax

#thank you!

# No prob! Thanks for volunteering - you did great :D
# LMK if you have any questions about anything

# I have to delete this code in a week, so pls copy it if
# you want to keep it for posterity

def maxValueBottomUp(root):
  min = float("-inf")
  if not root:
    return min
  leftMax = maxValueBottomUp(root.left) if root.left else min
  rightMax = maxValueBottomUp(root.right) if root.right else min
  return max(root.val, leftMax, rightMax)

print(f"max value bottom up: {maxValueBottomUp(node50)}")
    
