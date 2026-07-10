


class Solution:
    def isValid(self, s: str) -> bool:
        opens = "([{"
        closes = ")]}"
        close_to_open = {")": "(", "]": "[", "}": "{"}
        stack = []
        for character in s:
            if character in opens:
                stack.append(character)
                continue

            if character in closes:
                if stack and stack[-1] == close_to_open[character]:
                    stack.pop()
                else:
                    return False

        return not stack
    
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False


class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {"(" : ")", "{" : "}", "[" : "]"}
        stack = ["#"]
        for char in s:
            if char in open_to_close:
                stack.append(char)
                continue
            last_open_brackets = stack.pop()
            if char != open_to_close.get(last_open_brackets,""):
                return False
        return stack == ["#"]