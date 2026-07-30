
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count: dict[int, int] = {}
        for num in nums:
            if num not in nums_count:
                nums_count[num] = 1
            else:
                nums_count[num] += 1
        sorted_count = sorted(nums_count.items(), key=lambda x:x[1], reverse=True)

        return [item[0] for item in sorted_count[:k]]
