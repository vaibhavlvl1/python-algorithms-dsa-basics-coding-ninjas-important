# TC best case - O(n)
# worst case - O(n2)

arr = [9,8,7,6,1,2,5,4,3]
n = len(arr)


def bubble_sort(arr):
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


bubble_sort(arr)

print(arr)