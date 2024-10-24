class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

head1 = Node(4, Node(3, Node(2, None)))
while head1:
    #print(head1.value)
    head1 = head1.next

#P2 Find Frequency
def count_element(head, val):
    d = {}
    while head:
        if head.value in d:
            d[head.value] += 1 
        else:
            d[head.value] = 1
        head = head.next
    return d.get(val)



head2 = Node(3, Node(1, Node(2, Node(1, None))))
print(count_element(head2, 1))


print("-------------------------------")


#P3 Remove Tail
# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


# I have a bug! 
def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 
		
	# Start from the head and find the second-to-last node
    current = head
    while current.next.next: 
        current = current.next

    current.next = None # Remove the last node by setting second-to-last node to None
    return head



head3 = Node(3, Node(1, Node(2, Node(1, None))))

#using the online visual python debugger we notice the logic is right but the print statement does not reflect the changes
def printNodeVals(head:Node):
    while head:
        print(head.value)
        head = head.next

printNodeVals(head3)
remove_tail(head3)
print("------------")
printNodeVals(remove_tail(head3))




#P4 Find the Middle 
def find_middle_element(head):
	pass





head3 = Node(3, Node(1, Node(2, Node(1, None))))

