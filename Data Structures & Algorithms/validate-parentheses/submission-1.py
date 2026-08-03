class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            if c in closeToOpen: # it's a closed bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop() # a valid pair found!
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
        