class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Initialize the left pointer of the window
        left = 0
        # Tracks the current sum of the window
        current_sum = 0
        # Initialize result with a value larger than any possible length
        res = float('inf')
        
        for right in range(len(nums)):
            # 1. Expand the window by adding the current element
            current_sum += nums[right]
            
            # 2. Shrink the window while the condition is met
            while current_sum >= target:
                # Update the minimum length found so far
                res = min(res, right - left + 1)
                
                # Subtract the leftmost element and move the pointer
                current_sum -= nums[left]
                left += 1
        
        # 3. If res was never updated, return 0; otherwise return res
        return res if res != float('inf') else 0