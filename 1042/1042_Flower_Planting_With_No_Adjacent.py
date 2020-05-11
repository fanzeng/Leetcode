class Solution(object):
    # At first I did not understand the problem description correctly and thought a path can contain many segments.
    # In fact, for this problem, it's fine to have the same flower when gardens are only connected by paths more than 1 segment long.
    # i.e., if no direct path exists, they can have same flower.
    # So below is a solution to a different problem, where gardens are deemed connected as long as there is a way to get from one to the other.
    # def gardenNoAdj(self, N, paths):
    #     """
    #     :type N: int
    #     :type paths: List[List[int]]
    #     :rtype: List[int]
    #     """
    #     d_flower = {}
    #     d_set_to_garden = {}
    #     d_garden_to_set = {}
    #
    #     set_count = 0
    #     for path in paths:
    #         g0 = path[0]
    #         g1 = path[1]
    #         if d_garden_to_set.get(g0) is not None:
    #             set_id = d_garden_to_set[g0]
    #             d_garden_to_set[g1] = set_id
    #             d_set_to_garden[set_id].add(g1)
    #         elif d_garden_to_set.get(g1) is not None:
    #             set_id = d_garden_to_set[g1]
    #             d_garden_to_set[g0] = set_id
    #             d_set_to_garden[set_id].add(g0)
    #         else:
    #             d_garden_to_set[g0] = set_count
    #             d_garden_to_set[g1] = set_count
    #             d_set_to_garden[set_count] = set([g0, g1])
    #             set_id = set_count
    #             set_count += 1
    #     print d_set_to_garden
    #     for set_connected_gardens in d_set_to_garden.values():
    #         list_connected_gardens = list(set_connected_gardens)
    #         flower = 1
    #         for g in list_connected_gardens:
    #             d_flower[g] = flower
    #             flower += 1
    #     res = [d_flower[i] for i in xrange(1, N+1)]
    #     return res

    def gardenNoAdj(self, N, paths):
        d_flower = {}
        d_available_flower = {}
        for i in xrange(1, N+1):
            d_available_flower[i] = [1, 2, 3, 4]

        d_path = {}
        for i in xrange(1, N+1):
            d_path[i] = []

        for path in paths:
            if path[0] > path[1]:
                d_path[path[1]].append(path[0])
            else:
                d_path[path[0]].append(path[1])

        # without loss of generality, we can always assign 1 to 1st garden, since answer is guaranteed to exist.
        d_flower[1] = 1
        to_remove = []
        for path in d_path[1]:
            if 1 in d_available_flower[path]:
                d_available_flower[path].remove(1)


        for i in xrange(2, N+1):
            list_available_flower = d_available_flower[i]
            chosen_flower = list_available_flower[0]
            d_flower[i] = chosen_flower
            for path in d_path[i]:
                if chosen_flower in d_available_flower[path]:
                    d_available_flower[path].remove(chosen_flower)

        res = [d_flower[i] for i in xrange(1, N+1)]
        return res

test = Solution()
print test.gardenNoAdj(3, [[1,2],[2,3],[3,1]]) # possible solution: [1,2,3]
print test.gardenNoAdj(4, [[1,2],[3,4]]) # possible solution: [1,2,1,2]
print test.gardenNoAdj(4, [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]) # possible solution: [1,2,3,4]
print test.gardenNoAdj(8, [[1,2],[2,3],[3,4],[5,6],[6,7],[7,8]]) # possible solution: [1,2,3,4,1,2,3,4]
print test.gardenNoAdj(5, [[4,1],[4,2],[4,3],[2,5],[1,2],[1,5]]) # possible solution: [1,2,1,3,3]