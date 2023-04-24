from collections import deque
from typing import List, Tuple

def round(remaining_points: int, remaining_deq: deque) -> Tuple[int, int]:
    if len(remaining_deq) == 0:
        raise Exception('should not be here dude')
    left = remaining_deq[0]
    right = remaining_deq[-1]
    if len(remaining_deq) == 2:
        return (max(left, right), 0)
    else:
        # case if I pop left
        points_to_get_left = remaining_points - left
        pop_left_copy = remaining_deq.copy()
        pop_left_copy.popleft()
        next_guy_left, me_left = round(points_to_get_left, pop_left_copy)

        # case if I pop right
        points_to_get_right = remaining_points - right
        pop_right_copy = remaining_deq.copy()
        pop_right_copy.pop()
        next_guy_right, me_right = round(points_to_get_right, pop_right_copy)

        if (points_to_get_left + me_left - next_guy_left) > (points_to_get_right + me_right - next_guy_right):
            return (points_to_get_left + me_left, next_guy_left)
        else:
            return (points_to_get_right + me_right, next_guy_right)
            
def stoneGameVII(stones: List[int]) -> int:
    remaining_points = sum(stones)
    deq = deque(stones)
    alice, bob = round(remaining_points, deq)
    return abs(alice - bob)

if __name__ == '__main__':
    print('Input in format: 1,3,4,5')
    inp = input()
    inp.strip()
    split_str = inp.split(',')
    arr = [int(c) for c in split_str]
    print(stoneGameVII(arr))

