# https://leetcode.com/problems/course-schedule/description/
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        taken = 0
        visited = [False]*numCourses

        relationships = dict(set)
        for prereq in prerequisites:
            relationships[prereq[0]].add(prereq[1])

        def cycle_detection(node: int) -> bool:
            
            visited[node] = -1 # means visiting
            for course in relationships[node]:
                if visited[course] == -1:
                    return False
                
            visited[node] = True
            