# to find if an element is present in singly linked lists

# ITERATIVE SOLUTION

def linked_list_find(head, target):
    while head != None:
        if head.data == target:
            return True
        head = head.next
    return False

# RECURISVE SOLUTION

def recursive_find(head, target):
     
    if head == None:
        return False
    
    if head.val == target:
        return True
    
    # recursive calling
    return recursive_find(head.next, target)