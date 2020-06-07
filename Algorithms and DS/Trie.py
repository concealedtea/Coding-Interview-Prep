# Tries are used to store items (usually strings) based on prefixes in common
# O(n) lookup to see if a word is in the trie where n
class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode("*")
    
    # Adds word to Trie
    def addWord(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = TrieNode(letter)
            curr_node = curr_node.children[letter]
        curr_node.isEnd = True
    
    # Checks if word is in Trie
    def isInTrie(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        return curr_node.isEnd

trie = Trie()
words = ["wait", "waiter", "shop", "shopper"]
for word in words:
    trie.addWord(word)

print(trie.isInTrie("wait"))
print(trie.isInTrie("waite"))
print(trie.isInTrie("shop"))
print(trie.isInTrie("hello"))