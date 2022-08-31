import time as t
import random as r
import Quick_Sort as qs
import Merge_Sort as ms


l = []
for i in range(1000):
    l.append(r.randint(1, 5000))
list1 = l.copy()
list2 = l.copy()


start = t.time()

ms.mergeSort(list1)

end = t.time()

total = end - start
print(f"First sort took {total} seconds to complete")

start = t.time()

qs.quickSort(0, len(list2) - 1, list2)

end = t.time()

total = end - start
print(f"Second sort took {total} seconds to complete")



