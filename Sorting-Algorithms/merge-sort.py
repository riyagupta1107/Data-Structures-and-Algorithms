def Merge(left,right,arr):
    i,j,k=0,0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            print(arr[k])
            i=i+1
        else:
            arr[k]=right[j]
            print(arr[k])
            j=j+1
        k=k+1
    while i<len(left):
        arr[k]=left[i]
        print(arr[k])
        i=i+1
        k=k+1
    while j<len(right):
        arr[k]=right[j]
        print(arr[k])
        j=j+1
        k=k+1
    print(arr)


def mergeSort(arr):
    n=len(arr)
    if n<2:
        return
    mid=n//2
    left=arr[:mid]
    right=arr[mid:n]
    mergeSort(left)
    mergeSort(right)
    Merge(left,right,arr)

mergeSort([2,4,6,1,5,3,8,7])