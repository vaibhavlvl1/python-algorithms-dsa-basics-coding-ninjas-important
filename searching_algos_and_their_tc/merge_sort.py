# tc of merge sort is best and worst nlogn

# merge sort


arr= [9,8,7,1,2,6,5,4,3]
n = len(arr)

def merge(mat1,mat2,arr):
    a = 0
    b = 0
    c = 0
    
    while a<len(mat1) and b<len(mat2):
        if mat1[a]<mat2[b]:
            arr[c] = mat1[a]
            a+=1
            c+=1
        else:
            arr[c]=mat2[b]
            c+=1
            b+=1
    while a<len(mat1):
        arr[c]=mat1[a]
        c+=1
        a+=1
    while b<len(mat2):
        arr[c] = mat2[b]
        c+=1
        b+=1

        


def merge_sort(arr):
    if len(arr)==1:
        return arr
    
    mid = len(arr)//2
    a = arr[mid:]
    b = arr[:mid]

    merge_sort(a)
    merge_sort(b)

    merge(a,b,arr)

# main

merge_sort(arr)
print(arr)