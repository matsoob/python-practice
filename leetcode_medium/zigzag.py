from typing import List


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.list = list()
        p1 = 0
        p2 = 0
        while p1 < len(v1) or p2 < len(v2):
            if p1 < len(v1):
                self.list.append(v1[p1])
                p1 += 1
            if p2 < len(v2):
                self.list.append(v2[p2])
                p2 += 1
        self.pointer = -1

    def next(self) -> int:
        self.pointer += 1
        return self.list[self.pointer]

    def hasNext(self) -> bool:
        return self.pointer < len(self.list) - 1
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())