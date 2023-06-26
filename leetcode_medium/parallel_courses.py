# https://leetcode.com/problems/parallel-courses/

from collections import defaultdict
from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        if not relations:
            return 1
        prerec_dict = defaultdict(set)
        unlock_dict = defaultdict(set)
        done_set = set()
        check_as_prio = set(range(1, n+1))
        for relation in relations:
            prerec_dict[relation[1]].add(relation[0])
            unlock_dict[relation[0]].add(relation[1])
            if relation[1] in check_as_prio:
                check_as_prio.remove(relation[1])
        current_sem_count = 0
        while len(done_set) < n:
            current_sem_count += 1
            takable = set()
            for course in check_as_prio:
                if course not in prerec_dict:
                    takable.add(course)
                else:
                    prerecs = prerec_dict[course]
                    if all([prerec in done_set for prerec in prerecs]):
                        takable.add(course)
            check_as_prio = set()
            for course in takable:
                done_set.add(course)
                for maybe_unlocked in unlock_dict[course]:
                    check_as_prio.add(maybe_unlocked)
            if not takable:
                return -1
        return current_sem_count   



if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumSemesters(3, [[1,3],[2,3]])) # expect two
    print(sol.minimumSemesters(3, [[1,2],[2,3],[3,1]])) # expect two
    