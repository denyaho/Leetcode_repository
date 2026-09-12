
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)
        if n < m:
            larger_nums = nums2
            smaller_nums = nums1
        elif n >= m:
            larger_nums = nums1
            smaller_nums = nums2
        larger_nums = sorted(larger_nums)
        intersection = []
        for num in smaller_nums:
            if num in intersection:
                continue
            left, right = 0, len(larger_nums)-1
            while left <= right:
                mid = (right + left) //2
                if num > larger_nums[mid]:
                    left = mid + 1
                elif num < larger_nums[mid]:
                    right = mid - 1
                else:
                    intersection.append(num)
                    break

        return intersection