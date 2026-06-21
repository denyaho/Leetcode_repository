class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth_largest = k
        self.sort_list = nums

    def add(self, val: int) -> int:
        self.sort_list.append(val)
        self.sort_list.sort(reverse=True)
        return self.sort_list[self.kth_largest - 1]

# Your KthLargest object will be instantiated and called as