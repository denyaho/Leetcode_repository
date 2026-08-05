import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return
        heap = [(nums1[i] + nums2[0], i , 0) for i in range(min(k, len(nums1)))]
        heapq.heapify(heap)
        k_pair_smallest_sum = []
        while len(k_pair_smallest_sum) < k and heap:
            _, i, j = heapq.heappop(heap)
            k_pair_smallest_sum.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return k_pair_smallest_sum