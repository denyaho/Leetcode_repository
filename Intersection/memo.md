# 問題
 https://leetcode.com/problems/intersection-of-two-arrays/

# 問題概要
 nums1, nums2 の二つの数値配列が与えられる。
 この二つの数値配列に共通する数値を新たな配列に入れreturnする。

## step1

初めは、nums1,nums2にそれぞれどのような数値が入っているのかを確認したかったので、
collections.defaultdict(int)を用いてdict型にした。

その後は、nums1(nums2でもどっちでもいいが)の各要素をforで回していき、
nums1, nums2のdictの両方に合致する要素を答えの配列に入れることにした。


時間計算量: resultの大きさはmin(n, m)
           nums1の大きさをnとするとO(n * min(n, m))
空間計算量: nums1_to_count, nums2_to_countの大きさをそれぞれ n, mとすると、O(n + m)
```
import collections
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_to_count = collections.defaultdict(int)
        nums2_to_count = collections.defaultdict(int)
        for num in nums1:
            nums1_to_count[num] += 1
        for num in nums2:
            nums2_to_count[num] += 1
        
        result = []
        for num in nums1:
            if num in nums1_to_count and num in nums2_to_count and num not in result:
                result.append(num)
        return result
```

## step2

* setを使う場合(https://github.com/ksaito0629/leetcode_arai60/blob/349_intersection_of_two_arrays/349_intersection_of_two_arrays/memo.md)

時間計算量: O(n + m)
空間計算量: O(n + m)

intersectionを使っても、 &　を使った積集合でも同じ

```
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        return list(nums1_set & nums2_set)

        # nums_intersection = nums1_set.intersection(nums2_set)
        # return list(nums_intersection)
```

* インデックスを用いる場合
 nums1, nums2をそれぞれ昇順にsortをする。
 その後、nums1, nums2をそれぞれインデックス i, jで管理し同期させながらincrementさせる。

 nums1[i], nums2[j]の値が異なる場合はnums1[i], nums2[j]のうち小さい値の方をインデックス加算させる。
 同じ値の場合は答えの配列に追加する

時間計算量: O(nlogn + mlogm)
空間計算量: O(n + m)

```

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_sorted = sorted(nums1)
        nums2_sorted = sorted(nums2)
        i = 0
        j = 0
        n = len(nums1)
        m = len(nums2)
        intersection = []
        while i < n and j < m:
            if nums1_sorted[i] < nums2_sorted[j]:
                i += 1
                continue
            if nums2_sorted[j] < nums1_sorted[i]:
                j += 1
                continue
            common_num = nums1_sorted[i]
            intersection.append(common_num)
            while i < n and nums1_sorted[i] == common_num:
                i += 1
            while j < m and nums2_sorted[j] == common_num:
                j += 1
        return intersection
```

https://github.com/aki235/Arai60/pull/13

* 参考コメント
  set作成の際のコストはO(n)なので、set自体のコストを考慮すると短い方を対象にする方が効率的

https://github.com/aki235/Arai60/blob/349-intersection-of-two-arrays/349_Intersection_of_Two_Arrays.md

問題を少々変え、片方をSortにして計算したりなど参考になる

半開区間
```
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
            left, right = -1, len(larger_nums)
            while right - left > 1:
                mid = (right + left) //2
                if num > larger_nums[mid]:
                    left = mid
                elif num < larger_nums[mid]:
                    right = mid
                else:
                    intersection.append(num)
                    break

        return intersection
```

閉区間で扱う場合
```

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
```