class Pokemon():
    def attack(self, opponent):
        opponent.hp = opponent.hp - self.damage
        if opponent.hp <= 0:
            print(f"{opponent.name} fainted.")
        else:
            print(f"{self.name} dealt {self.damage} damage to {opponent.name}")
    
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage




class Node:
    def __init__(self, value, next=None):
        self.value = value
        self. next = next
#Q1 Battle Pokemon
pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 

opponent = bulbasaur
pikachu.attack(opponent)

print("--------------------------------------")
#Q2 Convert to Linked List
node_2 = Node("Wigglytuff")
node_1 = Node("Jiggleypuff", node_2)

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next)


#Q3 Add first
def add_first(head, new_node):
    new_node.next = head
    head = new_node
    return new_node

# Using the Linked List from Problem 2
print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)

print(node_1.value, "->", node_1.next.value)


#Q4 Get Tail
'''
iterate using while loop updating tail until we tail.next == None (null)
'''
def get_tail(head):
    tail = head
    while tail.next != None:
        tail = tail.next
    return tail.value

# linked list: num1->num2->num3
num3 = Node(3, None)
num2 = Node(2, num3)
num1 = Node(1, num2)

head = num1
tail = get_tail(num1)
print(tail)



#Q5 Replace Node
'''
Iterate through linked list until we reach end of linked list replacing 
every Node matching the og Node and we 
replace it with replacemnet Node
'''
print("----------------------")
def ll_replace(head, original, replacement):
    curr = head
    while curr != None:
        if curr.value == original:
            curr.value = replacement
        print(curr.value)
        curr = curr.next


num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

head = num1
ll_replace(head, 5, "banana")
# updated linked list: "banana" -> 6 -> "banana"


#Q6 List Nodes TO DO
def listify_first_n(head :Node, n :int) -> list:
    lst = list()
    curr = head
    for node in range(n):
        lst.append(curr.value)
        curr = curr.next
    return lst


## linked list: a -> b -> c
#node_c = Node(a, node)
#node_b = Node(b, node_b)
#node_a = Node(a, b)
#
#head = a
#lst = listify_first_n(head,2)
#print(lst)
#
## linked list: j -> k -> l 
#head2 = j
#lst2 = listify_first_n(head2,5)
#print(lst2)
#

