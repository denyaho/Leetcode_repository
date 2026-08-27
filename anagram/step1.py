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