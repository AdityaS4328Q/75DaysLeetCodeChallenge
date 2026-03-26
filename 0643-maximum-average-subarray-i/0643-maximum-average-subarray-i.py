class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        SUM= sum(nums[:k])
        max_sum=SUM
        for i in range(k,n):
            SUM+=nums[i]
            SUM-=nums[i-k]
            max_sum=max(max_sum, SUM)
        return max_sum/k
