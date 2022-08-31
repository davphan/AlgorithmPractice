class BinarySearch:

    def recursive(self, arr, value, high, low):
        if low > high:
            return -1
        mid = (low + high) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            return self.recursive(arr, value, mid - 1, low)
        else:
            return self.recursive(arr, value, high, mid + 1)


    def iterative(self, arr, value):
        low = 0
        high = len(arr) - 1
        while high >= low:
            mid = (low + high) // 2
            if arr[mid] == value:
                return mid
            elif arr[mid] > value:
                high = mid - 1
            else:
                low = mid + 1
        return -1

if __name__ == '__main__':
    a = [1, 3, 4, 6, 7, 9, 13, 14, 16, 17, 19, 22]
    b = BinarySearch()
    x = 17
    print(b.recursive(a, x, len(a) - 1, 0))
    print(b.iterative(a, x))