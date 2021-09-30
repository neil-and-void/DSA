class TrieNode:
    def __init__(self):
        self.chars = [None] * 26
        self.end = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        n = len(word)
        letterNode = self.root
        for i in range(n):
            key = ord(word[i]) - ord('a')
            if letterNode.chars[key] is None:
                letterNode.chars[key] = TrieNode()
            letterNode = letterNode.chars[key]

        # change last letter node end to True
        letterNode.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        # iterate on letterNode until reached end of word and letternode end == true
        n = len(word)
        letterNode = self.root
        for i in range(n):
            key = ord(word[i]) - ord('a')
            letterNode = letterNode.chars[key]
            if letterNode == None:
                return False

        if letterNode.end == True:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        # iterate on letterNode until reached end of word
        n = len(prefix)
        letterNode = self.root
        for i in range(n):
            key = ord(prefix[i]) - ord('a')
            letterNode = letterNode.chars[key]
            if letterNode == None:
                return False
        return True

trie = Trie();
trie.insert("apple")
print(trie.search("apple"))   # return True
print(trie.search("app"))    # return False
trie.startsWith("app") #/ return True
trie.insert("app")
trie.search("app")  #/ return True

