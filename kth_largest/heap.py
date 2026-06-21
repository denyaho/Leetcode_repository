class Priority_Queue:
    def __init__(self):
        self.queue = []
    

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
            if right_idx < len(self.queue) and self.queue[right_idx] > self.queue[left_idx]:
                child_idx = right_idx
            else:
                child_idx = left_idx
            if last <= self.queue[child_idx]:
                break
            self.queue[idx] = self.queue[child_idx]
            idx = child_idx
        self.queue[idx] = last

        return top

if __name__ == "__main__":
    heap = Priority_Queue()
    heap.push(5)
    heap.push(3)
    heap.push(7)
    heap.push(1)
    print(heap.top())  # Output: 7
    heap.pop()
    print(heap.top())
    heap.push(11)
    print(heap.top())  # Output: 11