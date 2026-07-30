# 問題
https://leetcode.com/problems/top-k-frequent-elements/


# Step1

* 問題の概要として、numsという配列において、出現頻度の多い要素を一番多い要素からK番目まで取得する

* 制限としては、O(nlogn)より少ない計算量で行うこと

* 計算量制限を無視して、出現頻度を計算するために辞書を用い、出現した頻度ごとにカウントするようにした。
* その後、pythonのsorted関数(tim sort)を用いてO(nlogn)で降順でソートを行い、K番目までをリストとしてreturn

初期はsort(tim sort)を用いて実装
```
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}
        for num in nums:
            if num not in nums_count:
                nums_count[num] = 1
            else:
                nums_count[num] += 1
        sorted_count = sorted(nums_count.items(), key=lambda x:x[1], reverse=True)

        return [item[0] for item in sorted_count[:k]]

```

+ バケットソートを使用した解法

```
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_frequencies = Counter(nums)

        max_frequency = max(num_to_frequencies.values())

        bucket = [[] for _ in range(max_frequency + 1)]
        for num, freq in num_to_frequencies.items():
            bucket[freq].append(num)

        result = []
        for i in range(len(bucket) - 1, 0, -1):
            result.extend(bucket[i])
            if len(result) > k:
                return result[:k]
        return result
```

* heapを用いた解法
```
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_frequencies = Counter(nums)

        result = []
        for num, freq in num_to_frequencies.items():
            heapq.heappush(result, (freq, num))
            if len(result) > k:
                heapq.heappop(result)
        return [num for _, num in result]
```

```
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, _ in Counter(nums).most_common(k)]
```

* heapのnlargestを用いた解法
```
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_frequencies = Counter(nums)
        sorted_counter = heapq.nlargest(k, num_to_frequencies.items(), key=lambda x:x[1])
        return [num for num, _ in sorted_counter]
```


# Step2

##　他の人のプルリク

①
https://github.com/kazuki-official/leetcode/blob/347-top-k-frequent-elements/memo.md

* 同率k位がたくさんある場合

https://github.com/potrue/leetcode/pull/9/files#r2083755650


②

https://github.com/ksaito0629/leetcode_arai60/pull/5


* クイックセレクトについて(常識らしいので必読)

https://discord.com/channels/1084280443945353267/1183683738635346001/1185972070165782688

参考資料
https://web.engr.oregonstate.edu/~huanlian/algorithms_course/1-datastructures/quicksort_BST.html


③

https://github.com/naoto-iwase/leetcode/pull/9

* SWEの常識からやや逸脱しているかもしれませんがLomuto's partitionは全ての値が等しい場合、区間が１つずつしか狭まっていかないのでランダムにピボットを取ってもO(N^2)になるというのがありました。
これはHoare's Partitionを使うかDutch National Flag Partitionを使うことで解決できるようです。

https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme
https://cs.stackexchange.com/questions/11458/quicksort-partitioning-hoare-vs-lomuto/11550

④
https://github.com/hayashi-ay/leetcode/pull/60/changes

```
quickselect。Time Complexityは~O(nlogn)~ ← Average: O(n), Worse(n^2)になる。
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def partition(freq, left, right, pivot_index):
            sorted_index = left
            pivot_value = freq[pivot_index][0]
            freq[pivot_index], freq[right] = freq[right], freq[pivot_index]
            for i in range(left, right):
                value = freq[i][0]
                if value > pivot_value:
                    freq[i], freq[sorted_index] = freq[sorted_index], freq[i]
                    sorted_index += 1
            freq[sorted_index], freq[right] = freq[right], freq[sorted_index]
            return sorted_index

        def quick_select(freq, left, right, k):
            if left > right:
                return
            pivot_index = random.randint(left, right)
            sorted_index = partition(freq, left, right, pivot_index)
            if sorted_index == k:
                return
            elif sorted_index > k:
                quick_select(freq, left, sorted_index, k)
            else:
                quick_select(freq, sorted_index + 1, right, k)
            

        freq_dict = Counter(nums)
        freq_list = [ (count, num) for num, count in freq_dict.items()]
        quick_select(freq_list, 0, len(freq_list) - 1, k - 1)
        return [ num for count, num in freq_list[:k]]
```


# step3

quickselectを用いて実装

```
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def partition(freq, low, high, pivot_index):
            i = low - 1
            target_value = freq[pivot_index][0]
            freq[pivot_index], freq[high] = freq[high], freq[pivot_index]
            for j in range(low, high):
                cur_value = freq[j][0]
                if cur_value > target_value:
                    i += 1
                    freq[i], freq[j] = freq[j], freq[i]
            freq[i + 1], freq[high] = freq[high], freq[i + 1]
            return i + 1
        
        def quick_select(freq, low, high, k):
            if low >= high:
                return
            
            pivot_index = random.randint(low, high)
            sorted_index = partition(freq, low, high, pivot_index)
            if sorted_index == k:
                return
            elif sorted_index > k:
                quick_select(freq, low, sorted_index - 1, k)
            else:
                quick_select(freq, sorted_index + 1, high, k)
            
        num_to_freq = Counter(nums)
        num_to_freq_list = [(count, num) for num, count in num_to_freq.items()]
        quick_select(num_to_freq_list, 0, len(num_to_freq_list) - 1, k - 1)
        return [num for count, num in num_to_freq_list[:k]]
```