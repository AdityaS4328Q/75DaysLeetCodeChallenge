from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c_s1=Counter(s1)
        n= len(s1)
        x=0
        for i in range(len(s2)- len(s1)+1):
            s=s2[i:i+ len(s1)]
            
            if Counter(s)==c_s1:
                return True
            else:
                x+=1
                n+=1

        return False