class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store={}
        for i,num in enumerate(nums):
            req= target - num
            if req in store:
                return[store[req],i]
            store[num]=i