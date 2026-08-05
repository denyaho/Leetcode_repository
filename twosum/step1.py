class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_index = [(nums[i], i) for i in range(len(nums))]
        sorted_nums = sorted(nums_with_index)
        left, right = 0, len(nums) - 1
        while left < right:
            left_nums, index1 = sorted_nums[left]
            right_nums, index2 = sorted_nums[right]
            sum_of_nums = left_nums + right_nums
            if sum_of_nums == target:
                return [index1, index2]
            elif sum_of_nums > target:
                right -= 1
            elif sum_of_nums < target:
                left += 1
        