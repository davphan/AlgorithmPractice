class MinHeap(list):

    def __init__(self, arr:list):
        """Min heap data structure. Supports peek, insert, and delete functions.

        Instantiation Time complexity: O(nlog(n))
        Instantiation Space complexity: O(n)

        Args:
            arr (list): List of values to insert into the min heap.
        """
        super().__init__()
        for num in arr:
            self.insert(num)

    def peek(self):
        """Return the smallest value of the heap.
        Time complexity: O(1)

        Returns:
            Any: Smallest value of the heap.
        """
        return self[0]

    def insert(self, num):
        """Insert a new value into the heap.

        Time complexity: O(log(n))

        Args:
            num (Any): Value to be inserted into the heap.
        """
        # Add number to end of tree and track its index
        i = len(self)
        self.append(num)

        # Check if number is greater than its parent and is not at the top
        # of the tree, "bubbling up"
        while i > 0 and self[(i - 1) // 2] > num:

            # Swap number with parent
            self[(i - 1) // 2], self[i] = self[i], self[(i - 1) // 2]

            # Update index
            i = (i - 1) // 2

    def delete(self):
        """Deletes the smallest value from the top of the heap and returns the value

        Time Complexity: O(log(n))

        Returns:
            Any: Smallest value of the heap.
        """
        # Remove top element (max) and move last element to the top of the tree
        smallest = self[0]
        self[0] = self.pop()

        # Track current node and children
        i = 0
        left = 2 * i + 1
        right = 2 * i + 2

        # Decide which direction to "bubble down", the smallest child
        nextShift = left if left >= len(self) or right >= len(self) or self[left] < self[right] else right

        # Check if current node is larger than its smallest child, and swap
        # elements, "bubble down"
        while nextShift < len(self) and self[i] > self[nextShift]:

            # Swap current element with smallest child
            self[i], self[nextShift] = self[nextShift], self[i]

            # Re-track current node location and find next node location
            i = nextShift
            left = 2 * i + 1
            right = 2 * i + 2
            nextShift = left if left >= len(self) or right >= len(self) or self[left] < self[right] else right

        return smallest




import random

if __name__ == '__main__':
    arr = []
    for i in range(10):
        arr.append(random.randint(0, 20))
    heap = MinHeap(arr)
    print(f'Original array: {arr}')
    print(f'Min heap: {heap}')
    heap.insert(0)
    print(f'Insert 0: {heap}')
    heap.delete()
    print(f'Delete: {heap}')