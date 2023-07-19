# heap-sort

import random

# arr = [random.choice(range(0,15)) for i in range(10)]
arr = [5,4,3,2,7,8,9,1]



def heapify_up(arr,n,i):
    smallest = i

    rchild = 2*smallest+2
    lchild = 2*smallest+1

    if lchild<n and arr[lchild]<arr[smallest]:
        smallest = lchild
    elif rchild <n and arr[rchild]<smallest:
        smallest = rchild
    if smallest !=i:
        arr[smallest],arr[i] = arr[i],arr[smallest]
        heapify_up(arr,n,smallest)



def heapsort(arr):
    n = len(arr)
    for i in range(n-1//2,-1,-1):
        heapify_up(arr,n,i)
    
        print(f"After heapify:",arr)

    for i in range(n-1,-1,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify_up(arr,i,0)

        print(f"after rearranging: ",arr)

heapsort(arr)
print(arr)