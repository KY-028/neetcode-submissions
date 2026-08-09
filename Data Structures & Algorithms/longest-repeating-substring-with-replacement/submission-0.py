from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = defaultdict(int)
        max_freq = 0
        best = 0

        for r in range(len(s)):
            # Keep track of frequency
            count[s[r]] += 1

            # KEY: when do we shrink window?
            max_freq = max(max_freq, count[s[r]])
            while (r-l+1) - max_freq > k: # if the current "invalid characters" are too much
                # shrink, because max_freq will change next time, and no better best occur
                count[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
        return best
            
