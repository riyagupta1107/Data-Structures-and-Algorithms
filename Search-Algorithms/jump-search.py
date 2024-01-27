import math

def jumpSearch(arr,target):
    n=len(arr)
    #finding the step size to be jumped
    step=int(math.sqrt(n))
    prev=0
    current=step

    while current<n and arr[current]<=target:
        if arr[current]==target:
            return current
        prev=current
        current+=step
    for i in range(prev,current):
        if arr[i]==target:
            return i
    #If not found
    return -1  

#testing the code
print(jumpSearch([1,2,3,4,5,6,7,8,9],5))
