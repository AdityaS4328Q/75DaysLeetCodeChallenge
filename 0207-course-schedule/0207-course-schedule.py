class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a,b in pre:
            g[a].append(b)
        VISITED=2
        UNVISITED=0
        VISITING=1
        states=[UNVISITED]*numCourses
        def dfs(node):
            state = states[node]
            if state == VISITED: return True
            elif state == VISITING: return False
            states[node]=VISITING
            for nei in g[node]:
                if not dfs(nei):
                    return False
            states[node]= VISITED
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True