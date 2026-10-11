# 問題
https://leetcode.com/problems/subarray-sum-equals-k/description/

問題は、numsという整数配列と、kというターゲットとなる値が与えられるので
numsの部分配列で合計がkとなる部分配列の数を答えるという問題

# step1

部分配列を作成するということにとらわれ、subArrayを地道に計算し
subArrayの合計値がkとなった回数をカウントした。

見事にタイムアウト
時間計算量: O(n^2)
空間計算量: O(1)
```
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
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
```

次に、累積和を計算し、累積和の差分がkとなる場合をカウントした。
prefix[j] - prefix[i] == kとなる条件を探索

これもfor文を２回回したのでタイムアウト
``` 
import copy
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [0] * (len(nums) + 1)
        subArrayMap = defaultdict(int)
        for i in range(1, len(nums) + 1):
            prefixSum[i] += prefixSum[i - 1] + nums[i - 1]
        for i in range(len(prefixSum)):
            for j in range(i + 1, len(prefixSum)):
                subArrayMap[prefixSum[j] - prefixSum[i]] += 1
        
        return subArrayMap[k]

```

次に、AIと対話しながら解いた。

例として、nums = [1,2,3,4]としたときの累積和は[0,1,3,6,10]となる。
この場合、2番目から3番目までの部分配列は[2,3](indexでは1,2)であり、
その際の合計値は累積和のindex3からindex1を引いた数となる。

このような感じで、部分配列の合計値は累積和のある要素とある要素の引き算で考えることができる。
その際の式はprefix[j] - prefix[i] = kとなる。

この式を変更しprefix[i] = prefix[j] - kとする。
prefix[j]を現在の値、prefix[i]を過去の値とすると
累積和をfor文で回して、kで引き算した結果が過去に累積和としてカウントされているかを確認する。
カウントされていれば、その数をresultなどの変数に保存しておく。

時間計算量 O(n)
空間計算量 O(n)
```
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [0] * (len(nums) + 1)
        subArrayMap = defaultdict(int)
        result = 0
        for i in range(1, len(nums) + 1):
            prefixSum[i] += prefixSum[i - 1] + nums[i - 1]
        for i in range(len(prefixSum)):
            result += subArrayMap[prefixSum[i] - k]
            subArrayMap[prefixSum[i]] += 1
        return result
```

## step2

他の人のレポジトリを確認
https://github.com/katataku/leetcode/blob/560.-Subarray-Sum-Equals-K/560.%20Subarray%20Sum%20Equals%20K.md

やっていることは累積和とハッシュマップを利用した解法
```
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        accumulating_list = [0]
        for num in nums:
            accumulating_list.append(accumulating_list[-1] + num)

        result = 0
        num_to_previous_occurrence = defaultdict(int)
        for num in accumulating_list:
            complement_number = num - k
            result += num_to_previous_occurrence[complement_number]
            num_to_previous_occurrence[num] += 1
        return result
```

累積和をリストで事前に確保するのはメモリの無駄
```
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_sum_to_count = defaultdict(int)
        prefix_sum_to_count[0] = 1
        num_subarrays = 0
        for num in nums:
            prefix_sum += num
            num_subarrays += prefix_sum_to_count[prefix_sum - k]
            prefix_sum_to_count[prefix_sum] += 1

        return num_subarrays
```