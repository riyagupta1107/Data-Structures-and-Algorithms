def interpolationSearch(arr,target):
    low,high=0,len(arr)-1

    while low<=high and arr[low]<=target and arr[high]>=target:

        #putting the formula
        pos=low+(high-low)*(target-arr[low])/(arr[high]-arr[low])

        #check if the element is equal to the target number
        if arr[pos]==target:
            return pos
        
        #if the element is smaller than the target
        #search the right subarray
        elif arr[pos]<target:
            low=pos+1
        
        #if the element is greater than the target
        #search the left subarray
        else:
            high=pos-1