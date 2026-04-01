class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {')': '(', '}':'{', ']':'['}
        stack = []

        for c in s:
            if c in parentheses_map.values():
                stack.append(c)
            elif c in parentheses_map.keys():
                if not stack or parentheses_map[c] != stack.pop():
                    return False
        
        return not stack

        