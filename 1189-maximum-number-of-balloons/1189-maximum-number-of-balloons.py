from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count=Counter(text)

        for i in 'balloon':
            if i not in count:
                return 0
            else:
                return min(count['b'], count['a'],count['l']//2,count['o']//2,count['n'])