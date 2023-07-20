import random
# insertion sort
# TC WOrst = O(n2)
# TC BEst = O(n)

arr = [random.choice(range(50))for i in range(10)]
n = len(arr)
print(arr)

def insertion_sort(arr,n):
    for i in range(1,n):
        j = i-1
        key = arr[i]

        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

insertion_sort(arr,n)
print(arr)