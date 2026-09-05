class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev=0
        curr=0
        for i in range(2,n+1):
            prev, curr = curr, min(cost[i-2]+ prev, cost[i-1]+curr)

                

        return curr