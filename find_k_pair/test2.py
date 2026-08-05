
from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        visited = set()
        visited.add((0, 0))
        min_heap = [(nums1[0] + nums2[0], 0, 0)]
        k_pairs_with_smallest_sum = []
        def add_to_heap_if_necessary(x, y):
            if x < len(nums1) and y < len(nums2) and (x, y) not in visited:
                heapq.heappush(min_heap, (nums1[x] + nums2[y], x, y))
                visited.add((x, y))
    
        # 問題文的にはlen(k_pairs_with_smallest_sum)はk以上あるが,そうではないない場合を考慮して以下のように書くほうが望ましい.
        while len(k_pairs_with_smallest_sum) < k and min_heap:
            _, i, j = heapq.heappop(min_heap)
            k_pairs_with_smallest_sum.append([nums1[i], nums2[j]])
            add_to_heap_if_necessary(i + 1, j)
            add_to_heap_if_necessary(i, j + 1)

        return k_pairs_with_smallest_sum