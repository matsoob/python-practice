from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        unassigned_workers = set(range(len(workers)))
        unassigned_bikes = set(range(len(bikes)))
        worker_bike_assignment = [-1]*len(workers)
        all_distances = dict()
        # (distance, [(w, b)])
        for i, w_location in enumerate(workers):
            for j, b_location in enumerate(bikes):
                distance = abs(w_location[0] - b_location[0]) + abs(w_location[1] - b_location[1])
                if distance in all_distances:
                    all_distances[distance].append((i, j))
                else:
                    all_distances[distance] = [(i, j)]

        sorted_shortest_distances = list(all_distances.keys())
        sorted_shortest_distances.sort()
        for distance in sorted_shortest_distances:
            biker_worker_pairs = all_distances[distance]
            filtered_biker_worker_pairs = [pair for pair in biker_worker_pairs if pair[0] in unassigned_workers and pair[1] in unassigned_bikes]
            filtered_biker_worker_pairs.sort()
            for worker, bike in filtered_biker_worker_pairs:
                if worker in unassigned_workers and bike in unassigned_bikes:
                    worker_bike_assignment[worker] = bike
                    unassigned_workers.remove(worker)
                    unassigned_bikes.remove(bike)
                    if not unassigned_workers:
                        return worker_bike_assignment
            


        



if __name__ == '__main__':
    workers = [[0,0],[1,1],[2,0]]
    bikes = [[1,0],[2,2],[2,1]]
    sol = Solution()
    assert sol.assignBikes(workers, bikes) == [0,2,1]
    sol.assignBikes([[0,0],[2,1]], [[1,2],[3,3]]) == [1,0]