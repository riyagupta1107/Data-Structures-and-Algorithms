#finding an element with binary search

#ITERATIVE SOLUTION
def iterativeBS(array,target):
    low,high=0,len(array)-1
    while low<=high:
        mid=low+(high-low)//2
        #check if target is present at mid
        if array[mid]==target:
            return mid
        
        #if target is smaller than middle number,take left half
        elif array[mid]>target:
            high=mid-1
        
        #if target is greater than the middle number, take the right half
        else:
            low=mid+1
    
    #if target is not found in the array
    return -1

#RECURSIVE SOLUTION
def recursiveBS(array,target,low,high):
    if low<=high:
        mid=low+(high-low)//2

        #if element is at mid position
        if array[mid]==target:
            return mid
        
        #if target is smaller than the middle number
        #the target is present in left subarray
        elif array[mid]>target:
            return recursiveBS(array,target,low,mid-1)
        
        #if the target is greater than the middle number
        #the target is present in the right subarray
        else:
            return recursiveBS(array,target,mid+1,high)
    else:
        return -1
    