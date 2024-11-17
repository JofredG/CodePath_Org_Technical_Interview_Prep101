class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

from collections import deque 
def level_order(root):
    '''
      4
     / \
    2   6
   / \  
  1   3

    Understand
        input - root of binary tree
        output - list of bt nodes in level order traversal
    Match
        Breadth first search
        queue (for bfs)
    Plan
        Use in a helper function bfs to iterate through tree and add to list
    '''
    # If the tree is empty:
    # return an empty list
    if not root:
        return []

    # Create an empty queue using deque
    # Create an empty list to store the explored nodes
    queue = deque()
    ans_lst = []
    # Add the root to the queue
    queue.append(root)

    # While the queue is not empty:
    # Pop the next node off the queue (pop from the left side!)
    # Add the popped node to the list of explored nodes
    while(queue):
        currNode = queue.popleft()
        ans_lst.append(currNode.val)


        # Add each of the popped node's children to the end of the queue
        if currNode.left:
            queue.append(currNode.left)
        if currNode.right:
            queue.append(currNode.right)

    # Return the list of visited nodes
    return ans_lst


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print(level_order(root))

