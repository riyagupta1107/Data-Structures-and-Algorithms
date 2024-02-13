#Program to implement insertion sort

def insertionSort(arr):
    i = 1
    while i<len(arr):
        j = i-1
        small = arr[i]
        while j >= 0 and small < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = small
        i+=1
    return arr