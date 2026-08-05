class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_index = {}
        for i in range(len(nums)):
            nums_with_index[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_with_index and nums_with_index[complement] != i:
                return [i, nums_with_index[complement]]
