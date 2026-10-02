class Solution:
    def maxProfit(self, p: list[int]) -> int:
        m= p[0]
        profit=0
        for i in p:
            if m>=i:
                m=i
            else:
                profit+=(i-m)
                m=i
        return profit