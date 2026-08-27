import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStr_to_listStr = collections.defaultdict(list)
        for elem in strs:
            sorted_elem = "".join(sorted(elem))
            sortedStr_to_listStr[sorted_elem].append(elem)
        return [elem for elem in sortedStr_to_listStr.values()]