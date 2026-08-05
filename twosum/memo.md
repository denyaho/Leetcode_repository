# 問題
https://leetcode.com/problems/two-sum


## step1

問題としては、リストの中の２要素を使ってtargetと同じ値になる組み合わせを探索すること。

- 考えたこと
ソートされた数字の中で一番左(left)と一番右(right)のインデックスを定義し、
お互いに向かってループを回す。
nums[left] + nums[right]がtargetと同じであればreturnし、
targetより大きければrightを１減らす
targetより小さければleftを1増やす

ソートをしてしまうと、元のリストのインデックスが壊れてしまうので
値とインデックスをタプルで保持してからソートをした。


時間計算量はsortedが支配的より $O(n log n)$
時間計算量は $O(n)
```
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
```

## step2

HashMapを使えば $O(n)でできるので、Hashmapが最適

```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_index = {}
        for i in range(len(nums)):
            nums_with_index[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_with_index and nums_with_index[complement] != i:
                return [i, nums_with_index[complement]]
```

