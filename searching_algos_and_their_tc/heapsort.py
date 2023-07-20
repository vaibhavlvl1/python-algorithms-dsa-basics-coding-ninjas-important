import random

arr = [random.choice(range(50))for i in range(10)]
print(arr)
n = len(arr)


######## ascd order sort needs max_heap ####################

def heapify_up(arr,n,i):
    largest = i

    rchild = 2*i+2
    lchild = 2*i+1

    if lchild < n and arr[i] < arr[lchild]:
        largest = lchild
    if rchild < n and arr[largest] < arr[rchild]:
        largest = rchild

    if largest!=i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify_up(arr,n,largest)


def ascd_heapsort(arr):
    n = len(arr)

    for i in range(n//2-1,-1,-1):
        heapify_up(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify_up(arr,i,0)


# ascd_heapsort(arr)
# print(arr)

############### desd requires min heap ###################


def min_heapify_up(arr,n,i):
    smallest = i
    lchild  = 2*i+1
    rchild = 2*i+2

    if lchild<n and arr[smallest]>arr[lchild]:
        smallest = lchild

    if rchild < n and arr[smallest] > arr[rchild]:
        smallest = rchild

    if smallest != i:
        arr[i],arr[smallest] = arr[smallest],arr[i]
        min_heapify_up(arr,n,smallest)

def dscd_heapsort(arr):
    n = len(arr)

    for i in range((n-1)//2,-1,-1):
        min_heapify_up(arr,n,i)

    for i in range(n-1,-1,-1):
        arr[0],arr[i] = arr[i],arr[0]
        min_heapify_up(arr,i,0)


dscd_heapsort(arr)
print(arr)