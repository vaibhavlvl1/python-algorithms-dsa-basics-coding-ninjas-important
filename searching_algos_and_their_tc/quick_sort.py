# quick sort



def partition(si,ei,arr):
    pivot_ele = arr[si]

    c = 0
    for i in range(si+1,ei+1):
        if arr[i]<pivot_ele:
            c+=1
    
    pivot_index = c + si

    arr[si],arr[pivot_index] = arr[pivot_index],arr[si]

    l = 0
    m = len(arr)-1

    while l<m:
        if arr[l]<arr[pivot_index]:
            l+=1
        elif arr[m]>arr[pivot_index]:
            m+=1
        else:
            arr[l],arr[m] = arr[m],arr[l]


    return pivot_index

def quick_sort(si,ei,arr):
    if si>=ei:
        return
    
    pivot_index = partition(si ,ei,arr)

    quick_sort(si,pivot_index,arr)
    quick_sort(pivot_index + 1,ei,arr)



