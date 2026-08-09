from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        chars1, chars2 = [0] * 26, [0] * 26
        
        for i in range(len(s1)):
            chars1[ord(s1[i]) - ord('a')] += 1
            chars2[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if chars1[i] == chars2[i]:
                matches += 1
        # check each window
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index_l = ord(s2[l]) - ord('a')
            chars2[index_l] -= 1
            if chars2[index_l] == chars1[index_l]:
                matches += 1
            # if that removal was a mistake
            elif chars2[index_l] + 1 == chars1[index_l]:
                matches -= 1

            index_r = ord(s2[r]) - ord('a')
            chars2[index_r] += 1
            if chars2[index_r] == chars1[index_r]:
                matches += 1
            # if that addition was a mistake
            elif chars2[index_r] - 1 == chars1[index_r]:
                matches -= 1
            l += 1
        return matches == 26

            

        