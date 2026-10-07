from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_frequency = Counter(s)
        for i in range(len(s)):
            if char_to_frequency[s[i]] == 1:
                return i
        return -1