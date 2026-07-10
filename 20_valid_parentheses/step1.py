
#Runtime 1ms
#Memory 19.40 MB

#時間計算量 O(N)
#空間計算量 O(N)

##解法
#　スタックを用意する。スタックはリストで実装し、pop,appendで動作を再現
# 文字列を前から操作し、開き括弧があればif文で条件分けをしてスタックの中に対応する閉じ括弧があるかを検証
# 閉じ括弧があればスタックに要素を入れていき、最後まで捜査して、スタックに文字が残っていればFalseを返す。スタックが空であればTrueを返す。

from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        N = len(s)
        for i in range(N-1, -1, -1):
            if s[i] == '(' and stack:
                bracket = stack.pop()
                if bracket != ')':
                    return False
            elif s[i] == '[' and stack:
                bracket = stack.pop()
                if bracket != ']':
                    return False
            elif s[i] == '{' and stack:
                bracket = stack.pop()
                if bracket != '}':
                    return False
            else:
                stack.append(s[i])
        if stack:
            return False
        return True