# TC of binary search is 0(logn)
# best case O(1)

# binary search
# binary search requires a sorted array


arr = [1,2,3,4,5,6,7,8,9]


def binary_search(arr,k):
    lb = 0
    ub = len(arr)-1

    while lb<=ub:
        mid = (ub+lb)//2
        if arr[mid] == k:
            return True
        else:
            if arr[mid] > k:
                ub = mid-1
            else:
                lb = mid+1
    return False

print(binary_search(arr,10))