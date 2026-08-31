from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_fresh=0
        minute=-1
        m,n = len(grid), len(grid[0])
        rotten,fresh,empty=2,1,0
        q= deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==fresh:
                    num_fresh+=1
                elif grid[i][j]==rotten:
                    q.append((i,j))

        if num_fresh==0:
            return 0

        while q:
            q_size= len(q)
            minute+=1
            for _ in range(q_size):
                i,j = q.popleft()
                for r,c in [(i,j+1),(i+1,j),(i-1,j),(i,j-1)]:
                    if 0<=r<m and 0<=c<n and grid[r][c]==fresh:
                        q.append((r,c))
                        grid[r][c]= rotten
                        num_fresh-=1

        if num_fresh==0:
            return minute
        else:
            return -1
