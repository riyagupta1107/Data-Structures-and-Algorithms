import math

def jumpSearch(arr,target):
    n=len(arr)
    #finding the step size to be jumped
    step=math.sqrt(n)

    #finding the block where element is
    prev=0
    while arr[int(min(step,n))]<target:
        prev=step
        step+=math.sqrt(n)
        if prev>=n:
            return -1
        
    #doing a linear search
    while arr[int(prev)]<target:
        prev+=1
        if prev==min(step,n):
            return -1
        
    if arr[int(prev)]==target:
        return int(prev)

    return -1  

#testing the code
print(jumpSearch([1,2,3,4,5,6,7,8,9],5))
