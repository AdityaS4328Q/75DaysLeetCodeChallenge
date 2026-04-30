class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Map to store the length of the sequence a number belongs to
        # key: number, value: length of the sequence it's part of
        res = {}
        max_len = 0
        
        for n in nums:
            # Skip duplicates to avoid double-counting
            if n not in res:
                # Find the lengths of sequences to the left and right
                left = res.get(n - 1, 0)
                right = res.get(n + 1, 0)
                
                # The total length of the sequence n joins
                current_len = left + right + 1
                max_len = max(max_len, current_len)
                
                # Mark n as visited (value doesn't matter much here, but we set it)
                res[n] = current_len
                
                # Crucial step: Update the "outer limits" of the sequence
                # The boundary nodes now represent the new total length
                res[n - left] = current_len
                res[n + right] = current_len
                
        return max_len