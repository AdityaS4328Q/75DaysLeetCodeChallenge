class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        right=len(nums)-1
        left=0
        while left<right:
            if nums[left] + nums[right] > target:
                right-=1
            elif nums[left] + nums[right]< target:
                left+=1
            else:
                return [left+1, right+1]