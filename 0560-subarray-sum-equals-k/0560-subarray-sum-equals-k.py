class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # res stores the total count of subarrays
        res = 0
        # curr_sum tracks the prefix sum as we iterate
        curr_sum = 0
        # prefix_sums stores {prefix_sum : count_of_occurrences}
        # We initialize with {0: 1} to handle cases where a subarray 
        # starting from index 0 equals k.
        prefix_sums = {0: 1}
        
        for n in nums:
            curr_sum += n
            # Calculate the value we need to have seen previously
            diff = curr_sum - k
            
            # If diff exists in our map, add its frequency to our result
            res += prefix_sums.get(diff, 0)
            
            # Update the map with the current prefix sum
            prefix_sums[curr_sum] = 1 + prefix_sums.get(curr_sum, 0)
            
        return res