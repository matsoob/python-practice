from typing import List


class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1 and not edges:
            return True
        edge_dict = dict()
        for start, end in edges:
            if start in edge_dict:
                edge_dict[start].append(end)
            else:
                edge_dict[start] = [end]
        
        if destination in edge_dict:
            return False
        
        all_visited_set = set()
        current_pointers = [(source, set())]
        all_visited_set.add(source)
        while current_pointers:
            next_round = list()
            for pointer, visited_set in current_pointers:
                new_visited_set = set([*visited_set, pointer])
                if pointer not in edge_dict:
                    return False
                next_pointers = edge_dict[pointer]
                for next_pointer in next_pointers:
                    if next_pointer in new_visited_set:
                        return False
                    
                    if next_pointer != destination and next_pointer not in all_visited_set:
                        next_round.append((next_pointer, new_visited_set))
                        all_visited_set.add(next_pointer)
            # print("NEXT ROUND")
            # print(next_round)
            current_pointers = next_round
        return True

    # def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    #     if source == destination and not edges:
    #         return True

    #     edge_dict = dict()
    #     for start, end in edges:
    #         if start in edge_dict:
    #             edge_dict[start].append(end)
    #         else:
    #             edge_dict[start] = [end]
        
    #     if destination in edge_dict:
    #         return False
    #     def following_pointer
        
if __name__ == '__main__':
    sol = Solution()
    assert sol.leadsToDestination(4, [[0,1],[0,2],[1,3],[2,3]], 0, 3) is True
    assert sol.leadsToDestination(4, [[0,1],[0,3],[1,2],[2,1]], 0, 3) is False
    assert sol.leadsToDestination(3, [[0,1],[0,2]], 0, 2) is False
    assert sol.leadsToDestination(2, [[0,1],[1,1]], 0, 1) is False
    assert sol.leadsToDestination(1, [], 0, 0) is True
    assert sol.leadsToDestination(1, [[1,1]], 0, 0) is False
    assert sol.leadsToDestination(5, [[0,1],[0,2],[0,3],[0,3],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]], 0, 4) is True