from typing import List


def game_recursion(piles: List[int]) -> bool:
    def turn_max(curr: int, i: int, j: int) -> int:
        if abs(i-j) == 1:
            return max(piles[i], piles[j])
        return max(piles[i] + (curr - turn_max(curr - piles[i], i+1, j)), piles[j] + (curr - turn_max(curr - piles[j], i, j-1)))
    
    high_score = turn_max(sum(piles), 0, len(piles) - 1)
    if (high_score*2 > sum(piles)):
        return True
    else:
        return False
    

if __name__ == '__main__':
    print('Input in format: 1,3,4,5')
    inp = input()
    inp.strip()
    split_str = inp.split(',')
    arr = [int(c) for c in split_str]
    print(game_recursion(arr))
