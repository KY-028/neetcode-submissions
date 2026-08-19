class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        found = False

        def backtrack(s, visited, r, c):
            nonlocal found
            # protect out of bounds
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return
            # don't revisit
            if (r, c) in visited:
                return
            
            # now let's try to add this letter
            s += board[r][c]

            if word == s:
                found = True
                return

            # if this addition is useless, leave
            if not word.startswith(s):
                return

            visited.add((r, c))

            dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]

            for d in dirs:
                backtrack(s, visited, r + d[0], c + d[1])

            visited.remove((r, c))

        # try every block as starting character
        for r in range(len(board)):
            for c in range(len(board[0])):
                backtrack("", set(), r, c)
                if found:
                    return True

        return found