class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(','}':'{',']':'['}
        stack = []

        for bracket in s:
            if bracket in hashmap:
                if not stack:
                    return False
                top = stack.pop()
                if hashmap[bracket] != top:
                    return False
            
            else:
                stack.append(bracket)

        if stack:
            return False
        else:
            return True
        