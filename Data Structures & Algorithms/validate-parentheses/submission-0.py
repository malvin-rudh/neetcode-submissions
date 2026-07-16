class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '{':'}', '[':']'}
        stack = []

        for char in s:
            if char == ')' or char == ']' or char == '}':
                if stack:
                    if brackets[stack[-1]] == char:
                        stack.pop()
                        continue
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False