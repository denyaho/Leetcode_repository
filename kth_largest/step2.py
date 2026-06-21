import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth_largest = k
        self.heap = []
        
        for num in nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) > self.kth_largest:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.kth_largest:
            heapq.heappop(self.heap)
        return self.heap[0]
