class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        max_empty_len_front = 0
        i = 0
        while seats[i] == 0:
            max_empty_len_front += 1
            i += 1
        max_empty_len_mid = 0
        empty_len = 0
        for seat in seats:
            if seat == 0:
                empty_len += 1
            else:
                if empty_len > max_empty_len_mid:
                    max_empty_len_mid = empty_len
                empty_len = 0
        if seats[-1] == 0:
            max_empty_len_back = empty_len
        else:
            max_empty_len_back = -1
        return max([max_empty_len_front, max_empty_len_back, (max_empty_len_mid-1) / 2 + 1])


test = Solution()
print test.maxDistToClosest([1,0,0,0,1,0,1]) # 2
print test.maxDistToClosest([1,0,0,0]) # 3
print test.maxDistToClosest([0,1]) # 1
print test.maxDistToClosest([0,0,0,0,0,1]) # 5