# 問題
https://leetcode.com/problems/group-anagrams

* 問題概要
文字列のリストが渡されるので、アナグラムごとにグループ化させる

## step1

- 考えたこと

アナグラムになる文字はソートさせた場合に全て同じ文字列になるということに着目し、
各文字をソートさせて一つのkeyとし、valueにリストとしてソートさせる前の文字列を入れ込む処理を行った。

時間計算量
 sortedの計算量が文字列の文字数をkとして、$O(k log k)
 for文の計算量が $O(n)
 よって、$O(n * k log k)
空間計算n
 $O(n)
```
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStr_to_listStr = {}
        for elem in strs:
            sorted_elem = "".join(sorted(elem))
            if sorted_elem not in sortedStr_to_listStr:
                sortedStr_to_listStr[sorted_elem] = [elem]
            else:
                sortedStr_to_listStr[sorted_elem].append(elem)
        return [elem for elem in sortedStr_to_listStr.values()]
```

## step2

defaultdictを用いてコードを短縮

```
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStr_to_listStr = collections.defaultdict(list)
        for elem in strs:
            sorted_elem = "".join(sorted(elem))
            sortedStr_to_listStr[sorted_elem].append(elem)
        return [elem for elem in sortedStr_to_listStr.values()]
```