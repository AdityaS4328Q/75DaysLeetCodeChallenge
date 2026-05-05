class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the array to use two-pointer logic
        nums.sort()
        # Initialize closest_sum with the sum of the first three elements
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If we find the exact target, return it immediately
                if current_sum == target:
                    return current_sum
                
                # Update closest_sum if the current_sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on how current_sum compares to target
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum