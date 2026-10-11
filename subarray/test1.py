class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subArrayMap = []
        result = 0
        for i in range(len(nums)+1):
            subArraySums = 0
            for j in range(len(nums)):
                if i + j >= len(nums):
                    break
                subArraySums += nums[i + j]
                if subArraySums == k:
                    result += 1
        return result