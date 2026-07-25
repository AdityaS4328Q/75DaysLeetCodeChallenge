class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n= len(nums)
        max_num=0
        curr_zero=0
        l=0
        for r in range(n):
            if nums[r]==0:
                curr_zero+=1

            while curr_zero>k:
                if nums[l]==0:
                    curr_zero-=1
                l+=1

            w = r-l+1

            max_num =max(max_num,w)
        return max_num