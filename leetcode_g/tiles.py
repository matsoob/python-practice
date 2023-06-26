from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = Counter(tiles)
        print(counter)
        def depth_first(counter: Counter):
            possibilities = 0
            for key in counter.keys():
                if counter[key] > 0:
                    counter[key] -= 1
                    possibilities += depth_first(counter) + 1
                    counter[key] += 1
            return possibilities     
        return depth_first(counter)
        

    # def wordsFromWord(self, length: int, word: str) -> int:
    #     counter = Counter(word)
    #     if length == 1:
    #         return counter.__len__

        

            

if __name__ == '__main__':
    sol = Solution()
    print(sol.numTilePossibilities("AAB"))
    assert sol.numTilePossibilities("AAABBC") == 188
    assert sol.numTilePossibilities("V") == 1