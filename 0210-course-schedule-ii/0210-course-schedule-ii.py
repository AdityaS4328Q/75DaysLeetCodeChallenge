class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        visiting, visited, unvisited = 1,2,0
        states = [unvisited]*n
        order=[]
        g= defaultdict(list)
        for a,b in pre:
            g[a].append(b)
        def dfs(i):
            if states[i]==visiting:
                return False
            elif states[i]==visited:
                return True
            states[i]=visiting

            for nei in g[i]:
                if not dfs(nei):
                    return False
            states[i]=visited
            order.append(i)
            return True


        for i in range(n):
            if not dfs(i):
                return []
        return order