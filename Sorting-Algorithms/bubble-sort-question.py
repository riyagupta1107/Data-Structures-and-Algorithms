#Question
'''You are given an array of size N and an integer M. You have to calculate the
difference between the maxmum and minimum sum of M elements.
Suppose there is an array
array=[5,7,8,3,1,6,2]
the size of the array: N=7
let the value of M=2

maximum sum=15
minimum sum=3
answer= max-min=12'''

#Approach
'''1. Sort the array in ascending order.
2. Calculate the sum of first M elements which is the minimum sum.
3. Calculate the sum of last M elements which is the maximum sum.
4. Calculate the difference between the maximum sum and the minimum sum.'''

#Sorting the array using bubble sort
def bubbleSort(arr):
    i=0
    while i<len(arr):
        j=0
        while j<len(arr)-i-1:
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            j+=1
        i+=1
    return arr
#Calculating the minimum sum
def minSum(arr,M):
    l1=bubbleSort(arr)
    minsum=0
    for num in range(0,M):
        minsum+=l1[num]
    return minsum
#Calculating the maximum sum
def maxSum(arr,M):
    l1=bubbleSort(arr)
    maxsum=0
    N=len(arr)
    for num in range(N,N-M-1,-1):
        maxsum+=l1[num]
    return maxsum
#Calculating the difference
array=[6,7,8,9,4,7,4,3]
max=maxSum(array,2)
min=maxSum(array,2)
diff=max-min
print(diff)