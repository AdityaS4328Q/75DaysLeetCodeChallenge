class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # This is exactly the same as the standard Trie insert
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        # We use a nested helper function for DFS traversal
        def dfs(index, node):
            curr = node
            
            for i in range(index, len(word)):
                char = word[i]
                
                if char == '.':
                    # If it's a dot, we must check ALL possible children
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    # If none of the children paths matched, return False
                    return False
                else:
                    # Standard Trie traversal for normal characters
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
                    
            # After finishing the word, check if we landed on a valid end node
            return curr.is_end_of_word

        # Start the DFS from index 0 and the root of the Trie
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)