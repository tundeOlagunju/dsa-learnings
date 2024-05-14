import collections
# https://leetcode.com/problems/implement-trie-prefix-tree/solution/
# https://leetcode.com/problems/word-search-ii/ -- and boggle backtracking,trie,dfs
class TrieNode:
    def __init__(self) -> None:
        self.is_word = False
        self.word = None # you can store the word here or trace it back when you need it
        self.children = collections.defaultdict(TrieNode)
        

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        for c in word:
            current = current.children[c]
        current.is_word = True
        current.word = word
    
    def starts_with(self, prefix):
        current = self.root
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        return True

    def search(self, word):
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.is_word
    
    # https://leetcode.com/problems/design-add-and-search-words-data-structure/
    # search when '.' can be matched with any character
    def search(self, word): 
    
        def dfs(word, curr):
            for i, char in enumerate(word):
                if char in curr.children:
                    curr = curr.children[char]
                elif char == '.':
                    for child in curr.children.values():
                        is_word = dfs(word[i+1:], child)
                        if is_word:
                            return True
                    # if no nodes lead to answer from '.' dont give other nodes any chance, return false. Check mistake in prev solution submitted
                    return False
                # if character != . 
                else: return False
            return curr.is_word

        return dfs(word, self.root)
    
    # search when '.' can be matched with any character -> recursive way
    def search(self, word):
        def dfs(node, i):
            if i == len(word): return node.end_node
               
            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i+1): return True
                    
            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)
            
            return False
    
        return dfs(self.root, 0)


    
    def delete(self, word):
        if not self.search(word):
            return
        self.root = self._delete(self.root, word, 0)
    
    def _delete(self, trienode, word, d):
        if trienode is None:
            return None
        if d == len(word) and trienode.is_word:
            trienode.is_word = False
        else:
            c = word[d]
            trienode.children[c] = self._delete(trienode.children[c], word, d+1)
        
        # to_be_deleted_keys = []
        # for key, value in trienode.children.items():
        #     if not value:
        #         to_be_deleted_keys.append(key)
        
        # for i in to_be_deleted_keys:
        #     del trienode.children[i]

        # delete entries where value is None i.e Nodes whose TrieNode has been set to None but still have key (i.e character)
        trienode.children = collections.defaultdict(TrieNode, {k: v for k, v in trienode.children.items() if v}) # defaultdict is needed here because self.children is a defaultdict

        if trienode.is_word:
            return trienode
        
        for value in trienode.children.values():
            if value:
                return trienode
        
        return None
    
    def longest_prefix_of(self, word):
        current = self.root
        last_word_seen = ""
        for c in word:
            if c not in current.children:
                return last_word_seen
            else:
                current = current.children[c]  
            if current.is_word:
                last_word_seen = current.word
        return current.word if current.is_word else last_word_seen
        

    def words_that_match(self, prefix):
        current = self.root
        for c in prefix:
            if c not in current.children:
                return []
            current = current.children[c]
        
        self._level_order_print(current)


    def level_order_print(self):
        self._level_order_print(self.root)

    def _level_order_print(self, trienode):
        current = trienode
        if not current:
            print("Trie is empty")
            return
        queue = collections.deque()
        queue.append(current) 
  
        while queue:
            current = queue.popleft()
            if current.is_word: 
                print(current.word)
            queue.extend(list(current.children.values()))
        


trie = Trie()
trie.insert("eat")
trie.insert("shells")
trie.insert("eats")
trie.insert("she")
trie.delete("eats")
trie.insert("dog")
trie.insert("a")

# trie.delete("s")
trie.insert("eats")

# print(trie.longest_prefix_of("eatsssssss"))
# print(trie.longest_prefix_of("shells"))
# print(trie.longest_prefix_of("adidas"))
# print(trie.longest_prefix_of("shellsort"))
# print(trie.longest_prefix_of("shelter"))

trie.words_that_match("e")
trie.words_that_match("shells")
# print(trie.search("shells"))
# print(trie.starts_with("sh"))
# trie.level_order_print()
