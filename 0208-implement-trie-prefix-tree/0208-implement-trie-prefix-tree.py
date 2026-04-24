class TrieNode:
    def __init__(self):
        # A dictionary to hold the children nodes (character -> TrieNode)
        self.children = {}
        # A boolean flag to mark if a word ends at this specific node
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        # Initialize the Trie with an empty root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            # If the character isn't a child yet, create a new node
            if char not in curr.children:
                curr.children[char] = TrieNode()
            # Move down to that child node
            curr = curr.children[char]
        # Mark the last node as the end of the newly inserted word
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            # If a character is missing, the word isn't in the tree
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # Return True ONLY if we actually ended on a completed word
        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            # If a character in the prefix is missing, return False
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # If we successfully traversed the whole prefix, it exists
        return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)