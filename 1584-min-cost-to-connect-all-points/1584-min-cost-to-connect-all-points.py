import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        seen=set()
        total_dist=0
        min_heap=[(0,0)]

        while len(seen)<n:
            dist,i = heapq.heappop(min_heap)
            if i in seen:
                continue
            seen.add(i)
            total_dist +=dist
            xi,yi = points[i]

            for j in range(n):
                if j not in seen:
                    xj,yj = points[j]
                    dist= abs(xi-xj) + abs(yi-yj)
                    heapq.heappush(min_heap, (dist,j))

        return total_dist