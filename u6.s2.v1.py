#Problem 1: Detect Circular Linked List

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(head):
    visited = set()
    while head.next:
        if head in visited:
            return True
        visited.add(head)
        head = head.next
    return False


# Problem 2: Find Last Node in a Linked List Cycle
def find_last_node_in_cycle(head):
    visited = set()
    while head.next():
        if head.next in visited:
            return head
        visited.add()
        head = head.next
    return None


# num1 -> num2 -> num3 -> num1
n3 = Node(3,None)
n2 = Node(2, n3)
head2CircularList = Node(1, n2)
n3.next = head2CircularList
print(is_circular(head2CircularList))

# var1 -> var2 -> var3
head = Node(1, Node(2, Node(3, None)))
print(is_circular(head))

print("____________________________________________")

##num1 -> num2 -> num3 -> num4 -> num2
#n4 = Node(4, None)
#n3 = Node(3, n4)
#n2 = Node(2, n3)
#n1 = Node(1, n2)
#n4.next = n1
#
#print(find_last_node_in_cycle(n1))
