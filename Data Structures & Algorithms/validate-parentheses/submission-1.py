class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False 
        s = s.strip()

        d = {"{": "}",
        "}": "{",
        "(": ")",
        ")": "(",
        "[": "]",
        "]": "["
        }
        stack = [-1]
        for b in s:
            target = d[b]
            if b == "}" or b == "]" or b == ")":
                if stack[-1] != target:
                    return False
            if stack[-1] == target:
                stack.pop()
            else:
                stack.append(b)
            print(stack)
        
        if stack[-1] == -1:
            return True
        else:
            return False