# 問題
https://leetcode.com/problems/first-unique-character-in-a-string/

# step1
問題として、与えられた文字列の中で冗長ではない文字のうち、一番最初に現れた文字の位置(インデックス)を返す関数を作る

* 時間計算量
 文字列の長さをnとすると、O(n)
* 空間計算量
 O(n)
```
from collections import defaultdict
from typing import List

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = defaultdict(int)
        for i in range(len(s)):
            char_count[s[i]] += 1
        print(char_count)
        for i in range(len(s)):
            if char_count[s[i]] == 1:
                return i
        return -1
```

# step2

* 参考
　https://github.com/ksaito0629/leetcode_arai60/blob/387_first_unique_character_in_a_string/387_first_unique_character_in_a_string/memo.md
 
 defaultdict-> pythonの辞書は元々要素の順番を保持しないらしく、バージョン3.7から順番を保持するようになるとのこと。
 

OrderedDictを使った解法
OrderedDictについて(https://github.com/python/cpython/blob/main/Lib/collections/__init__.py)
```
from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        unique = OrderedDict()

        for i, char in enumerate(s):
            if char in seen:
                unique.pop(char, None)
                continue
            unique[char] = i
            seen.add(char)
        
        if not unique:
            return -1
        
        _, first_unique_char_idx = unique.popitem(last=False)
        return first_unique_char_idx
```

Counterを用いて、各文字の出現回数をカウント後、
一番最初にカウント数１の要素が来た際にreturnする
```
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_frequency = Counter(s)
        for i in range(len(s)):
            if char_to_frequency[s[i]] == 1:
                return i
        return -1
```