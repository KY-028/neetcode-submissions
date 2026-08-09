class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        dup = set()
        best = 0
        while r < len(s):
            # while this character has not been removed
            while s[r] in dup:
                dup.remove(s[l])
                l += 1
            dup.add(s[r])
            best = max(best, r - l + 1)
            r += 1
        return best
