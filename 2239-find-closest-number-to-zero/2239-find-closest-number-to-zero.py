class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        c=nums[0]
        for i in nums:
            if abs(c)>abs(i):
                c=i
        if c<0 and abs(c) in nums:
            return abs(c)
        else:
            return c
