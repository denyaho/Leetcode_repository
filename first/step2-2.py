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