class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backtrack(s, opens, closes):
            if closes > opens or opens > n:
                return
            if closes == opens == n:
                ans.append(s)
                return
            
            backtrack(s + "(", opens + 1, closes)
            backtrack(s + ")", opens, closes + 1)
        
        backtrack("", 0, 0)
        return ans

