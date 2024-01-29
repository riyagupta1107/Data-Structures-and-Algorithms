#Bubble Sort Algorithm
#arranging the list in ascending order.

def bubblesort(arr):
    i=0
    while i<len(arr):
        j=0
        while j<len(arr)-i-1:
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            j+=1
        i+=1
    return arr

#main
l1=[3,5,9,2,7,1,6,8,4]
print(bubblesort(l1))  