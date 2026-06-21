from typing import List


class HeapSort:

    def __init__(self, array):
        self.array = array
    
    def _swap(self, i: int, j: int) -> None:
        self.array[i], self.array[j] = self.array[j], self.array[i]
        return
    
    def heapify(self, i: int, n: int) -> None:
        left_child = 2 * i + 1
        if left_child >= n:
            return
        
        if left_child + 1 < n and self.array[left_child] < self.array[left_child + 1]:
            left_child += 1
        
        if self.array[left_child] < self.array[i]:
            return
        
        self._swap(i, left_child)
        self.heapify(left_child, n)
    
    def sort(self) -> List[int]:
        n = len(self.array)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(i, n)
        
        for i in range(n - 1, 0, -1):
            self._swap(0, i)

            self.heapify(0, i)
        return self.array

if __name__ == "__main__":
    array = [3, 2, 1, 5, 6, 9, 4]
    heap_sort = HeapSort(array)
    print(heap_sort.sort())