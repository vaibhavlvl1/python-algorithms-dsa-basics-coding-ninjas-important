import random
# selection sort

# TC worst = O(n2)
# TC BEST = O(n2)

arr = [random.choice(range(100))for i in range(10)]
n = len(arr)
print(arr)

def selection_sort(arr,n):
    for i in range(n):
        minimum = i
        for j in range(i+1,n):
            if arr[j]<arr[minimum]:
                minimum = j
        arr[i],arr[minimum] = arr[minimum],arr[i]

selection_sort(arr,n)

print(arr)
