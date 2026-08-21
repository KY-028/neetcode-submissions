class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if not endWord in wordList or beginWord == endWord:
            return 0

        adj = defaultdict(list)
        
        # Go through every word and put the word under the patterns
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                adj[pattern].append(word)
            

        # 
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            # layer: every word in the deque
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                # now try to find the neighbours of this word
                # explore all patterns and other words
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    # gather all neighbours
                    for nei in adj[pattern]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
            res += 1 # layer
        return 0


