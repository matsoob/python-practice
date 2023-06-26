# https://leetcode.com/problems/meeting-rooms-ii/
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_times = list()
        end_times = list()

        for interval in intervals:
            start_times.append(interval[0])
            end_times.append(interval[1])
        start_times.sort()
        end_times.sort()
        current_meeting_count = 0
        max_meeting_count = 0

        start_time_pointer = 0
        end_time_pointer = 0
        while start_time_pointer < len(start_times):
            if start_times[start_time_pointer] < end_times[end_time_pointer]:
                start_time_pointer += 1
                current_meeting_count += 1
                max_meeting_count = max(max_meeting_count, current_meeting_count)
            else:
                end_time_pointer += 1
                current_meeting_count -= 1

        return max_meeting_count

