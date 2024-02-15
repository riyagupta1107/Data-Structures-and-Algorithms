class Node:

    # Function to intialize the node object.
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # intialize next as null

# Linked list class 
class LinkedList:

    # Function to initialize linked list object
    def __init__(self):
        self.head = None 

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

# A -> B -> C-> D -> NULL

def printLinkedList(head):
    current=head
    while current != None:
        print(current.data)
        current=current.next

def recursiveLinkedList(head):
    if head == None:
        return 
    print(head.data)
    recursiveLinkedList(head.next)

recursiveLinkedList(a)