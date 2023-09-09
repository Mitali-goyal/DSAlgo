class TrieNode:
    def __init__(self):
        # Initialize a TrieNode with 26 possible children (for each letter of the alphabet)
        self.children = [None] * 26
        # 'end' flag indicates whether a word ends at this node
        self.end = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Initialize the Trie with a root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root  # Start from the root of the Trie
        for c in word:
            i = ord(c) - ord("a")  # Convert the character to an index (0-25)
            if curr.children[i] == None:
                # If the child node doesn't exist, create it
                curr.children[i] = TrieNode()
            curr = curr.children[i]  # Move to the child node
        curr.end = True  # Mark the end of the inserted word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root  # Start from the root of the Trie
        for c in word:
            i = ord(c) - ord("a")  # Convert the character to an index (0-25)
            if curr.children[i] == None:
                # If the child node doesn't exist, the word is not in the Trie
                return False
            curr = curr.children[i]  # Move to the child node
        return curr.end  # Check if the last node marks the end of a word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root  # Start from the root of the Trie
        for c in prefix:
            i = ord(c) - ord("a")  # Convert the character to an index (0-25)
            if curr.children[i] == None:
                # If the child node doesn't exist, no word starts with this prefix
                return False
            curr = curr.children[i]  # Move to the child node
        return True  # The prefix exists in the Trie, and there might be words that start with it
