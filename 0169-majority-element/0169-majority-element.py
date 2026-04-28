class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        count = 0
        
        for n in nums:
            # If count is 0, we pick the current number as our new candidate
            if count == 0:
                res = n
            
            # If current number matches candidate, increment count
            # Otherwise, decrement count
            if n == res:
                count += 1
            else:
                count -= 1
                
        return res