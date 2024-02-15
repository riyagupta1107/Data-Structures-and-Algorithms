class Node:

    # Function to intialize the node object.
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # intialize next as null

# ITERATIVE APPROACH
def linkedListValues(head):
    values = list()
    curr = head

    # checking if the current node is not null
    while curr != None:

        # appending the node to values
        values.append(curr.data)

        #pointing to the next node
        curr = curr.next
    
    return values

# RECURSIVE APPROACH
def recursiveList(head):
    
    curr = head
    values = list()

    # if the current node is null.
    #if curr == None:
    #    return
    
    values.append(curr.data)
    recursiveList(curr.next)
    return values

# main
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

# A -> B -> C-> D -> NULL

print(recursiveList(a))