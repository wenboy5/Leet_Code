'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
'''


class TrieNode:
    def __init__(self):
        self.childNodes = {}
        self.isWordEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        we will start with root node and check for the first character
        if there is already a node present for the character we will fetch that node, else we will create a new node
        then we will iterate to next character
        """
        currNode = self.root
        for ch in word:
            node = currNode.childNodes.get(ch , TrieNode())
            currNode.childNodes[ch] = node
            currNode = node

        # after all the characters are traversed, mark the last node as end of word
        currNode.isWordEnd = True



    def search(self, word: str) -> bool:
        """
        we will start from root node and check for all the characters
        if we could not find a node for a character we will return False there
        once we iterate through all character we will check if that is a word end
        """

        currNode = self.root
        for ch in word:
            node = currNode.childNodes.get(ch)
            if  not node:
                return False
            currNode = node

        return currNode.isWordEnd


    def startsWith(self, prefix: str) -> bool:
        """
        starts with is similar to search except here we don't have to check whether the last character is end of word
        """
        currNode = self.root
        for ch in prefix:
            node = currNode.childNodes.get(ch)
            if not node:
                return False
            currNode = node

        return True