##　メモリ制限によりFail

import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]: 
        pairs_list = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):                
                sums_of_pair = (nums1[i] + nums2[j], (nums1[i], nums2[j]))
                heapq.heappush(pairs_list, sums_of_pair)
        
        return [nums for _, nums in heapq.nsmallest(k, pairs_list)]

## 修正版

import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        heap = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, len(nums1)))]
        heapq.heapify(heap)
        res = []
        while heap and len(res) < k:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        
        return res