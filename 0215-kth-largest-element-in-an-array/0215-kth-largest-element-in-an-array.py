import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans=0
        for i in range(len(nums)):
            nums[i]=-nums[i]

        heapq.heapify(nums)

        while k>0:
            ans= heapq.heappop(nums)
            k-=1

        return -ans