def mergeSort(array: list):
    if len(array) > 1:
        # split array into two sides
        mid = len(array) // 2
        arr1 = array[:mid]
        arr2 = array[mid:]

        # recursive call on left and right side, sorts arr1 and arr2
        mergeSort(arr1)
        mergeSort(arr2) 

        # tracks indeces for arr1, arr2, and array respectively
        i = j = k = 0

        # copy data from temp arrays onto main array of current method
        # call in sorted order
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                array[k] = arr1[i]
                i += 1
            else:
                array[k] = arr2[j]
                j += 1
            k += 1
        
        # sorts remaining elements of longer list
        while i < len(arr1):
            array[k] = arr1[i]
            i += 1
            k += 1

        while j < len(arr2):
            array[k] = arr2[j]
            j += 1
            k += 1


if __name__ == '__main__':
    a = [12, 11, 13, 5, 6, 7]
    print(f"Given Array: {a}")
    mergeSort(a)
    print(f"Sorted Array: {a}")