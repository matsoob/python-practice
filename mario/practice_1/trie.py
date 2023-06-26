from typing import List

class TrieNode:
    def __init__(self) -> None:
        self.is_leaf = False
        self.leaves = dict()

def build_trie(words: List[str]) -> TrieNode:
    root = TrieNode()
    if not words:
        return root
    for word in words:
        current = root
        pointer = 0
        while pointer < len(word):
            if word[pointer] not in current.leaves:
                current.leaves[word[pointer]] = TrieNode()
            current = current.leaves[word[pointer]]
            pointer += 1
        current.is_leaf = True
    return root


class Solution:
    def solve(self, target: str, all_words: List[str]) -> bool:
        if not target:
            return True

        trie = build_trie(all_words)
        unsplittable_tails = set()
        current_pointer = 0
        def split_from_here(root: TrieNode, pointer: int):
            node = root
            # if 
            if pointer in unsplittable_tails:
                return False
            while pointer < len(target):
                if node.is_leaf:
                    can_be_solved = split_from_here(root, pointer)
                    if can_be_solved:
                        return True
                    else:
                        unsplittable_tails.add(pointer)
                if target[pointer] in node.leaves:
                    node = node.leaves[target[pointer]]
                    pointer += 1
                else:
                    return False
            if pointer == len(target) and node.is_leaf:
                return True
            else:
                unsplittable_tails.add(pointer)
                return False

        return split_from_here(trie, current_pointer)


if __name__ == '__main__':
    sol = Solution()
    
    word_list = ['cat', 'ca', 'the', 'c', 'w','foo','bar']
    target = 'catthewfoobar'
    print(sol.solve(target, word_list))
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    print(sol.solve(s, wordDict))
    target = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    word_list = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print(sol.solve(target, word_list))