class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Take the first word as the reference
        first_word = strs[0]
        
        for i in range(len(first_word)):
            char = first_word[i]
            
            # Check this character against all other words
            for j in range(1, len(strs)):
                # If we reach the end of another word or find a mismatch
                if i == len(strs[j]) or strs[j][i] != char:
                    # Return the portion of the first word we've matched so far
                    return first_word[:i]
        
        # If the entire first word is a prefix for everything else
        return first_word