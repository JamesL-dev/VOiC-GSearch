"""This module defines and creates a Trie"""

#####################################################
# Trie Node Class
#####################################################
class TrieNode:
   """Trie Node constructor"""
   def __init__(self):
      """we initialize an array of pointers to each letter in the alphabet"""
      self.children = [None]*26

      """isEndOfWord is True if node represent the end of the word"""
      self.isEndOfWord = False


#####################################################
# Trie Class
#####################################################
class Trie:
   """Trie Constructor"""
   def __init__(self):
      """Init Tree"""
      self.root = self.getNode()
   
   #####################################################
   # getNode()
   #####################################################
   def getNode(self):
      """returns a new trie node init to NULL"""
      return TrieNode()

   #####################################################
   # charToIndex()
   #####################################################
   def _charToIndex(self,character):
      """private helper function
         Converts key current character into index
         use only 'a' through 'z' and lower case"""
      return ord(character) - ord('a')
   
   #####################################################
   # insert()
   #####################################################
   def insert(self,key):
      """If not present, inserts key into trie
		   If the key is prefix of trie node,
		   just marks leaf node"""
      pCrawl = self.root

      length = len(key)
      
      for level in range(length):
         index = self._charToIndex(key[level])
         
         """ if current character is not present """
         if not pCrawl.children[index]:
            pCrawl.children[index] = self.getNode()
         pCrawl = pCrawl.children[index]

      """ mark last node as leaf """
      pCrawl.isEndOfWord = True
   
   def search(self,key):
      """Search key in the trie
		   Returns true if key presents
		   in trie, else false"""

      pCrawl = self.root
      length = len(key)

      for level in range(length):
         index = self._charToIndex(key[level])
         if not pCrawl.children[index]:
            return False
         pCrawl = pCrawl.children[index]
      return pCrawl.isEndOfWord