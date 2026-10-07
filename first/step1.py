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