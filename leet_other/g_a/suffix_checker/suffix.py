from typing import List

class TrieNode:
    def __init__(self):
        self.leaves = dict()
        self.is_leaf = False

class StreamChecker:
    
    def add_word(self, word: str):
        if not word:
            return
        pointer = len(word) - 1
        trie_pointer = self.trie_root
        while pointer >= 0:
            if word[pointer] in trie_pointer.leaves:
                trie_pointer = trie_pointer.leaves[word[pointer]]
                pointer -= 1
            else:
                trie_pointer.leaves[word[pointer]] = TrieNode()
                trie_pointer = trie_pointer.leaves[word[pointer]]
                pointer -= 1
        trie_pointer.is_leaf = True
        
    def __init__(self, words: List[str]):
        self.words = words
        self.trie_root = TrieNode()
        self.current_query = list()
        for word in words:
            self.add_word(word)
        
    def query(self, letter: str) -> bool:
        self.current_query.append(letter)
        # print('CHECking ', self.current_query)
        return self.check_query()
        
    def check_query(self) -> bool:
        trie_pointer = self.trie_root
        query_pointer = len(self.current_query) - 1
        while query_pointer >= 0:
            if trie_pointer.is_leaf:
                return True
            elif self.current_query[query_pointer] in trie_pointer.leaves:
                trie_pointer = trie_pointer.leaves[self.current_query[query_pointer]]
                query_pointer -= 1
            else:
                return False
        return trie_pointer.is_leaf
                
if __name__ == '__main__':
    words = ["abaa","abaab","aabbb","bab","ab"]
    input = [["a"],["a"],["b"],["b"],["b"],["a"],["a"],["b"],["b"],["a"],["a"],["a"],["a"],["b"],["a"],["b"],["b"],["b"],["a"],["b"],["b"],["b"],["a"],["a"],["a"],["a"],["a"],["b"],["a"],["b"],["b"],["b"],["a"],["a"],["b"],["b"],["b"],["a"],["b"],["a"]]
    expected_output = [False,False,True,False,True,False,False,True,False,False,False,False,False,True,False,True,False,False,False,True,False,False,False,False,False,False,False,True,False,True,False,False,False,False,True,False,True,False,True,False]
    result = list()
    sc = StreamChecker(words)
    for i in input:
        res = sc.query(i[0])
        result.append(res)
    for i in range(len(result)):
        if expected_output[i] != result[i]:
            print("EXPECTED ", expected_output[i])
            print("GOT ", result[i])
            print("FOR ", input[i])
            print('AT ', i)
