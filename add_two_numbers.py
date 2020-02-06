'''
P: Given two linked lists in reverse order, add the number and return a linked list of the sum in reverse order.

E: 7 > 2 > 1  + 4 > 7 = 1 > 0 > 2

D:Node, linked list, int

A:  Given two linked lists
    Declare a root node variable ,a carry over variable and a pointer variable to the root node
        loop over the linked lists while they are truthy
            get the sum of each place in the list +  carry over over from the previous sum
        add data to next spot in list
    if anything left in carry over when both lists have no node
        final node = carry over
    return root node of new list

'''

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return str(f"Node: {self.data}")
        
def print_all_nodes(node:Node):
    current = node
    while current:
        print(current)
        current = current.next
    
def add_two_numbers(num1: Node, num2: Node) -> Node:
    root_node = Node((num1.data + num2.data) % 10)
    carry_over = (num1.data + num2.data) // 10
    node_holder = root_node
    while num1.next or num2.next:
        sum = (num1.next.data if num1.next else 0) + (num2.next.data if num2.next else 0) + carry_over
        node_holder.next = Node(sum % 10)
        if num1.next:
            num1 = num1.next
        if num2.next:
            num2 = num2.next
        node_holder = node_holder.next
        carry_over = sum // 10
    if carry_over:
        node.next = Node(carry_over)
    return root_node


l1 = Node(3)
l1.next = Node(2)
l1.next.next = Node(1)

l2 = Node(1)
l2.next = Node(1)
l2.next.next = Node(1)
print_all_nodes(add_two_numbers(l1,l2))  