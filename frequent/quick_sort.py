
class QuickSort:

    def __init__(self, arr):
        self.arr = arr

    def _swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        
## 最悪計算量になる可能性があるので注意
    def partition_high(self, low, high):
        pivot = self.arr[high]
        i = low -1
        for j in range(low, high):
            if self.arr[j] <= pivot:
                i += 1
                self._swap(i, j)
        self._swap(i + 1, high)
        return i + 1
    def sort(self, low=0, high=None):
        if high is None:
            high = len(self.arr) - 1
        if low < high:
            p = self.partition_high(low, high)
            self.sort(low, p - 1)
            self.sort(p + 1, high)

class QuickSort_median:

    def __init__(self, arr):
        self.arr = arr

    def _swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def _median_of_three(self, low, high):
        mid = low + (high - low) // 2
        if self.arr[low] > self.arr[mid]:
            self._swap(low, mid)
        if self.arr[low] > self.arr[high]:
            self._swap(low, high)
        if self.arr[mid] > self.arr[high]:
            self._swap(mid, high)
        self._swap(mid, high)

    def partition(self, low, high):
        self._median_of_three(low, high)
        pivot = self.arr[high]
        i = low - 1
        for j in range(low, high):
            if self.arr[j] <= pivot:
                i += 1
                self._swap(i, j)
        self._swap(i + 1, high)
        return i + 1

    def sort(self, low=0, high=None):
        if high is None:
            high = len(self.arr) - 1
        if low < high:
            p = self.partition(low, high)
            self.sort(low, p - 1)
            self.sort(p + 1, high)
    

arr = [10, 7, 8, 9, 1, 5, 3, 2, 4, 6]
arr = list(range(1000)) ## 一番右をピボットにする場合、すでにソート済みの配列を渡すと最悪計算量になる(1000だとRecursionError)。
qs = QuickSort(arr)
qs.sort()
print("Sorted array is:", qs.arr)