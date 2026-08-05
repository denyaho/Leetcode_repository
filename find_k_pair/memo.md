# 問題

https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

# step1

- 問題の制約として、「1 <= nums1.length, nums2.length <= 105」、
- nums1 and nums2 both are sorted in non-decreasing order

問題の制約として、上記の条件があるので、２重ループを行うとMLEとなってしまう。
また、nums1とnums2がsortedなので、愚直にループをするのではなく工夫が必要

しかし、解法が思いつかなかったので、一旦MLEのまま作成
```
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]: 
        pairs_list = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):                
                sums_of_pair = (nums1[i] + nums2[j], (nums1[i], nums2[j]))
                heapq.heappush(pairs_list, sums_of_pair)
        
        return [nums for _, nums in heapq.nsmallest(k, pairs_list)]

```

AIも活用しながら修正したのが以下の通り

- nums1の全要素とnums2の最左の要素でタプルをしてheap化(一番左が最も小さく、右に行くにつれて大きくなるので、徐々に右にずらしていき最小を取り出していく)

このコードでは、nums1の全探索していき、nums1の各要素とnums2の最小値をペアとしてヒープとして確保する。
nums2の最小値がすでにヒープに入っているので、次に最小となるのは一つ右の値となる。
ヒープの中にはすでにnums1[i]における最小合計値となる組み合わせが入っており、
nums2の次点での最小値を取り出した際に必ず同じか大きい値となる。
もしもnums1[i+1]+nums2[0]が(nums1[i]+nums2[j])などの探索した値よりも小さい場合は
heappopで出力されるため、考えられる組み合わせの中で最小のペアが毎回取り出される

時間計算量 $O(k log k)$
空間計算量 $O(k)$

```
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
```

# step2

https://github.com/hayashi-ay/leetcode/blob/hayashi-ay-patch-55/373.%20Find%20K%20Pairs%20with%20Smallest%20Sums.md

コードの内容としては、nums1,nums2はそれぞれソートされており、最小となる合計値はそれぞれnums1,nums2の一番最初の要素となる。
次点で最小合計値となる可能性があるのはnums1[i+1]+nums2[j], nums1[i]+nums2[j+1]となる。
なので、ループを回して、一つ一つ見ていく

表形式で見ていくと、重複するところがあるので、seenで重複の管理をしている
```
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        candidates = [(nums1[0] + nums2[0], 0, 0)]
        seen = set([(0, 0)])

        def need_to_add(x, y):
            if x >= len(nums1) or y >= len(nums2):
                return False
            if x == 0 or y == 0:
                return True
            return (x - 1, y) in seen and (x, y - 1) in seen
        
        def add_to_candidates_if_necessary(x, y):
            if need_to_add(x, y):
                heapq.heappush(candidates, (nums1[x] + nums2[y], x, y))

        pairs = []
        while len(pairs) < k and candidates:
            _, i, j = heapq.heappop(candidates)
            pairs.append([nums1[i], nums2[j]])
            seen.add((i, j))
            add_to_candidates_if_necessary(i + 1, j)
            add_to_candidates_if_necessary(i, j + 1)
        return pairs
```

参考PR
https://github.com/Yuto729/leetcode/blob/3e2f2d5850d9ea9bf5244acdf0176a05de4e7b0c/find-k-pairs-with-smallest-sums/main.md

> 実はvisitedが不要なやり方がある. nums1の最初のk行だけpushしておくと, (i,j)に対して(i,j+1)を探索すれば良くなるので重複することがなくなる.

visitedで管理するなら以下コードも綺麗
```
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
```