# https://leetcode.com/problems/gas-station/
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # O_n time here
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        if not gas:
            return -1
        pointer = 0
        while pointer < len(gas):
            if gas[pointer] - cost[pointer] < 0:
                pointer += 1
            else:
                current_gas = gas[pointer] - cost[pointer]
                next_pointer = (pointer + 1) % n
                # O_n^2 time :-(
                while next_pointer != pointer:
                    current_gas += gas[next_pointer] - cost[next_pointer]
                    if current_gas < 0:
                        break
                    next_pointer = (next_pointer + 1) % n
                if next_pointer == pointer:
                    return pointer
                else:
                    pointer += 1
        return -1
    

    def canCompleteCircuitFaster(self, gas: List[int], cost: List[int]) -> int:
        delta = list()
        n = len(cost)
        for i in range(n):
            delta.append(gas[i] - cost[i])
        
        last_start = 0
        in_the_tank = 0
        for i in range(n):
            in_the_tank += delta[i]
            if in_the_tank < 0:
                last_start = i+1
                in_the_tank = 0
        if last_start >= n or sum(gas) < sum(cost):
            return -1
        else:
            return last_start

