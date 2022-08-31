def partition(start, end, array: list):
    # start with initalizing pivot at beginning of array
    pivot_ind = start
    pivot = array[pivot_ind]

    # shift 'start' pointer until it crosses the 'end' pointer, then
    # swap pivot to end pointer
    while start < end:
        # push start pointer forward until greater than pivot
        while start < len(array) and array[start] <= pivot:
            start += 1
        # pull end pointer backwards until less than pivot
        while array[end] > pivot:
            end -= 1
        # swap start and end values if start and end ind haven't crossed
        # (tuple assignment)
        if (start < end):
            array[start], array[end] = array[end], array[start]

    # swap pivot element with end value
    array[end], array[pivot_ind] = array[pivot_ind], array[end]
    # return end pointer to divide array in two
    return end

def quickSort(start, end, array: list):
    if (start < end):
        p = partition(start, end, array)
        quickSort(start, p - 1, array)
        quickSort(p + 1, end, array)

if __name__ == '__main__':
    a = [10, 7, 8, 9, 1, 5]
    print(f"Inital List: {a}")
    quickSort(0, len(a) - 1, a)
    print(f"Sorted List: {a}")