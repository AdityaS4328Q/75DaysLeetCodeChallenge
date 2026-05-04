class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # l (low) tracks the right boundary for 0s
        # r (high) tracks the left boundary for 2s
        # i is our current iterator
        l, i = 0, 0
        r = len(nums) - 1
        
        while i <= r:
            if nums[i] == 0:
                # Found a 0, swap it to the 'low' boundary
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                # Found a 2, swap it to the 'high' boundary
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                # Important: Do NOT increment i here, because the 
                # new value swapped from the end needs to be checked.
            else:
                # Found a 1, just leave it and move on
                i += 1