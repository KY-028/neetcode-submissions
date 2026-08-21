class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list)
        
        for a, b in prerequisites:
            adj[a].append(b)

        visiting = set()
        def dfs(node):
            if node in visiting:
                return False
            
            # base case, no more required courses, this is the first course to take
            if adj[node] == []:
                return True
            
            # now trace more requirements up
            visiting.add(node)
            for pre in adj[node]:
                if not dfs(pre):
                    return False
            visiting.remove(node)
            # we do this because we already know all prereqs for this course is satisfiable
            adj[node] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True