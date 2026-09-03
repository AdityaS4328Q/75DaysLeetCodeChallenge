class Solution:
    def fib(self, n: int) -> int:
        prev=0
        curr=1
        if n==0:
            return 0

        for i in range(2,n+1):
            prev,curr=curr, prev+curr
        return curr