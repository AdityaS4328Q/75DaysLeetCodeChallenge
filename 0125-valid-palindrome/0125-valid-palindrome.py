class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean= []
        for c in s:
            if c.isalnum():               
                clean.append(c.lower())
        return clean==clean[::-1]