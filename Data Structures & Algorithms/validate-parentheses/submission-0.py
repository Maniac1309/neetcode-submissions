class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for char in s:
            if char in mapping:
                if not stack or stack[-1] != mapping[char]:# Closing bracket: stack must not be empty, and top must match
                    return False
                stack.pop() # Matching opening bracket found
            else:
                stack.append(char)#opening bracket
        return not stack# Valid only if every opening bracket was matched