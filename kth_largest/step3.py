#自作の優先度付きキューを使用して、KthLargestクラスを実装するコード

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)
    def __bool(self) -> bool:
        return len(self.queue) > 0

    def __getitem__(self, idx):
        return self.queue[idx]

    def push(self, val: int):
        self.queue.append(val)
        idx = len(self.queue) - 1
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.queue[parent_idx] <= val:
                break
            self.queue[idx] = self.queue[parent_idx]
            idx = parent_idx
        self.queue[idx] = val
    
    def top(self) -> int:
        if len(self.queue) != 0:
            return self.queue[0]
        return -1
    
    def show(self) -> None:
        print(self.queue)
    
    def pop(self) -> int:
        if len(self.queue) == 0:
            return -1
        top = self.queue[0]
        if len(self.queue) == 1:
            self.queue.pop()
            return top
        last = self.queue.pop()
        idx = 0
        while idx * 2 + 1 < len(self.queue):
            left_idx = idx * 2 + 1
            right_idx = idx * 2 + 2
            if right_idx < len(self.queue) and self.queue[right_idx] < self.queue[left_idx]:
                child_idx = right_idx
            else:
                child_idx = left_idx
            if last <= self.queue[child_idx]:
                break
            self.queue[idx] = self.queue[child_idx]
            idx = child_idx
        self.queue[idx] = last

        return top

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth_largest = k
        self.heap = Priority_Queue()
        
        for num in nums:
            self.heap.push(num)
            if len(self.heap) > self.kth_largest:
                self.heap.pop()

    def add(self, val: int) -> int:
        self.heap.push(val)
        if len(self.heap) > self.kth_largest:
            self.heap.pop()
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)