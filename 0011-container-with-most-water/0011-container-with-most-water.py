class Solution:
    def maxArea(self, height: List[int]) -> int:
        left  = 0                  # start pointer
        right = len(height) - 1   # end pointer
        max_water = 0
        
        while left < right:
            
            # Calculate current water
            width    = right - left
            h        = min(height[left], height[right])
            water    = width * h
            
            # Update maximum
            max_water = max(max_water, water)
            
            # Move the pointer with SHORTER line
            if height[left] < height[right]:
                left += 1    # left is shorter → move left inward
            else:
                right -= 1   # right is shorter (or equal) → move right inward
        
        return max_water