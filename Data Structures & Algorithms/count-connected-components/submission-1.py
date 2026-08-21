class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        """
        now we would have:
        0: 1
        1: 0, 2
        2: 0
        3: 4
        4: 3
        """

        # now attempt to iterate through clusters
        visited = set()
        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            # try to visit all its neighbours
            for n in adj[node]:
                dfs(n)

        components = 0
        for node in range(n):
            prev = len(visited)
            dfs(node)
            if len(visited) > prev:
                components += 1
        
        return components
