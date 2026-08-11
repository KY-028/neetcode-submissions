from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = defaultdict(int)
        for char in t:
            freq[char] += 1

        # start attempting to find a combo
        shortest = ""
        need = len(t)
        l = 0
        for r in range(len(s)):
            # search new letter, if needed, decrease
            if s[r] in freq:
                freq[s[r]] -= 1

                if freq[s[r]] >= 0:
                    need -= 1

            # if we now have a valid solution, compare and update
            while need == 0:
                if not shortest or r - l + 1 < len(shortest):
                    shortest = s[l:r+1]

                # now move left pointer as much as possible
                if s[l] in freq:
                    freq[s[l]] += 1

                    if freq[s[l]] > 0:
                        need += 1 # the need only restores if we now need this letter again

                l += 1


            # if s[r] in freq:
            #     # first update, l for first occurrence
            #     if l == -1:
            #         l = r
            #     freq[s[r]] -= 1
            #     # if at this point every character is found, update sol
            #     flag = False # are there still missing items?
            #     for letter, f in freq.items():
            #         if f > 0:
            #             flag = True
            #             break
            #     if not flag:
            #         if not shortest or r - l + 1 < len(shortest):
            #             shortest = s[l:r+1]
            #             while True:
            #                 # move left pointer
            #                 l += 1
            #                 if l >= len(s) or s[l] in freq:
            #                     freq[s[l]] += 1 # remove the leftmost char
            #                     break
        return shortest


            

                
