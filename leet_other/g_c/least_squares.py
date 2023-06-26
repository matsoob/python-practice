from functools import lru_cache
import math

class Solution:

    @lru_cache()
    def numSquares(self, n: int) -> int:
        num_to_check = math.floor(math.sqrt(n))
        if n - num_to_check**2 == 0:
            return 1
        current_min = None
        while num_to_check > 0:
            min_using_me = 1 + self.numSquares(n - num_to_check**2)
            if current_min is not None:
                current_min = min(min_using_me, current_min)
            else:
                current_min = min_using_me
            num_to_check -= 1
        return current_min


    def numSquares2(self, n: int) -> int:
        max_num_to_check = math.floor(math.sqrt(n))
        min_squares = [None]*(n+1)
        for i in range(1, max_num_to_check+1):
            square = i**2
            min_squares[square] = 1
        
        while min_squares[n] is None:
            current_new_recipes = list()
            for i in range(1, n+1):
                for j in range(i, n+1-i):
                    if None not in (min_squares[i], min_squares[j]):
                        new_num = i + j
                        can_make_with = min_squares[i] + min_squares[j]
                        current_new_recipes.append((new_num, can_make_with))
                        # if new_num == n:
                        #     return can_make_with
            for new_num, can_make_with in current_new_recipes:
                if min_squares[new_num] is None or min_squares[new_num] > can_make_with:
                    min_squares[new_num] = can_make_with
        return min_squares[n]

    def numSquares3(self, n: int) -> int:
        max_num_to_check = int(math.sqrt(n))
        min_squares = [float('inf')]*(n+1)
        squares = list()
        for i in range(1, max_num_to_check+1):
            square = i**2
            min_squares[square] = 1
            squares.append(square)
        for i in range(1, n+1):
            for square in squares:
                if i - square > 0:
                    min_squares[i] = min(min_squares[i - square] + 1, min_squares[i])
        return min_squares[n]

if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(12))
    print(sol.numSquares(13)) # should be 2, 4 + 9
    print(sol.numSquares3(10000)) # 1
    print(sol.numSquares3(7691))