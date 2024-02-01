'''This is code for selection sort'''

def selectionSort(arr):
    i=0
    while i<len(arr):
        j=i+1
        small=arr[i]
        pos=i
        while j<len(arr):
            if small>arr[j]:
                small=arr[j]
                pos=j
            j+=1
        arr[pos],arr[i]=arr[i],arr[pos]
        print("After iteration",i+1,"array is",arr)
        i+=1
    return arr

selectionSort([3,5,9,2,7,1,6,8,4])