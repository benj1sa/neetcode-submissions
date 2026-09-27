class Solution:
    def isValid(self, s: str) -> bool:
        bmap = {'}':'{', ']':'[', ')':'('}
        stack = []
        for c in s:
            if c in bmap: # if this is a closing paren
                if not stack or stack.pop() != bmap[c]: # pop it and check if it matches 
                    return False
            else:
                stack.append(c)
        return not stack