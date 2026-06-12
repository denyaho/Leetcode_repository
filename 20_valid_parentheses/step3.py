
##解法
# 1個目
## まず、スタックを用意する。スタックはリストで実装し、pop,appendで動作を再現
## 文字列を後ろから走査し、閉じかっこがあればスタックに追加する。
## 開きかっこがあれば、brackets_pairから対応する閉じかっこを取得し、一番最後にスタックに追加された文字と比較する。
## もし、異なればFalseを返す。最後まで操作して、スタックに文字が残っていれば括弧が閉じられていないのでFalseにする。スタックが空であれば、全ての括弧が正しく閉じられているのでTrueを返す。

#2個目
## 1個目の解法と同じだが、今回は文字列を前から操作する。
##　開き括弧があればスタックに追加し、right_bracketsにまとめた閉じ括弧の要素と同じであれば
## スタックの最後の要素と比較して、brackets_pairの組み合わせと異なればFalseを返す。
## 最後まで捜査して、スタックに文字が残っていればFalseを返す。スタックが空であればTrueを返す。


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        N = len(s)
        brackets_pair = {'(': ')', '[':']', '{':'}'}
        for i in range(N-1, -1, -1):
            if stack and s[i] in brackets_pair:
                if brackets_pair[s[i]] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack) == 0

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_pair = {')':'(', ']':'[', '}':'{'}
        right_bracket=")}]"
        for bracket in s:
            if stack and bracket in right_bracket:
                if brackets_pair[bracket] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(bracket)
        return len(stack) == 0