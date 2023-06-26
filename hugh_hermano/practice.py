
from collections import deque
import heapq
from typing import List


class Node:
    def __init__(self) -> None:
        self.left = None
        self.right = None

def get_max_width(root: Node) -> int:
    if not root:
        return 0
    current_layer = list()
    current_layer.append(root)
    current_max = 1
    while current_layer:
        next_layer = list()
        for node in current_layer:
            if node.left:
                next_layer.append(node.left)
            if node.right:
                next_layer.append(node.right)
        if len(next_layer) > current_max:
            current_max = len(next_layer)
        current_layer = next_layer
    return current_max

def get_max_length(layer: List[int]) -> int:
    if not layer:
        return 0
    curr = 0
    heap = []
    heapq.heappush(heap, (1, layer[0]))
    curr += 1
    while curr < len(layer):
        me = layer[curr]
        heap_pointer = 0
        while heap_pointer < len(heap):
            if heap[heap_pointer][1] > me:
                heapq.heappush(heap, (heap[heap_pointer][0] + 1, me))
                break
            heap_pointer += 1
        heapq.heappush(heap, (1, me))
        curr += 1
    print(heap)
    print(sorted(heap))
    longest = heapq.heappop(heap)
    return longest[0]


    # if not layer:
    #     return 0
    # current_max_contig = 0
    # pointer = 0
    # stack = list()
    # while pointer < len(layer):
    #     if not stack:
    #         stack.append(layer[pointer])      
    #     else:
    #         if stack[-1] > layer[pointer]:
    #             stack.append(layer[pointer])
    #         elif stack[-1] == layer[pointer]:
    #             pass
    #         else:
    #             current_max_contig = max(len(stack), current_max_contig)
    #             while stack and stack[-1] < layer[pointer]:
    #                 stack.pop()   
    #             stack.append(layer[pointer])
    #     pointer += 1
    # current_max_contig = max(len(stack), current_max_contig)
    # print(stack)
    # return current_max_contig

if __name__ == '__main__':
    input = [5, 8, 4, 9, 3, 1]
    print(get_max_length(input))