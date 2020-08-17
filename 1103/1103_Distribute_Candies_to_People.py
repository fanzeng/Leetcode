class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res = [0]* num_people
        i = 0
        candy_count = 0
        while candies > candy_count:
            candy_count += 1
            res[i] += candy_count
            candies -= candy_count
            i += 1
            i %= num_people
        res[i] += candies
        return res

test = Solution()
print test.distributeCandies(7, 4) # [1,2,3,1]
print test.distributeCandies(10, 3) # [5,2,3]
