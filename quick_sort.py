def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
array1 = [7,4,8,2,3,9,1,12]
print("Unsorted array:", array1)
sorted_array = quick_sort(array1)
print("Sorted array:", sorted_array)



