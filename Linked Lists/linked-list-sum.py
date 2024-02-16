class Node:

    # Function to intialize the node object.
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # intialize next as null


# To calculate sum of nodes in a singly linked list.

# ITERATIVE APPROACH

def sumList(head):

    sum = 0
    curr = head

    while curr != None:
        # adding the value of node to sum variable
        sum += int(curr.data)
        curr = curr.next
    
    return sum

# RECURSIVE APPROACH

def recursiveSum(head):

    # if head is null, then the sum is zero.
    if head == None:
        return 0
    
    #recursively returning the sum
    return head.data + sumList(head.next)
    

# main
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

# A -> B -> C-> D -> NULL

print(recursiveSum(a))
print(sumList(a))