class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #  Method 1 -------------------------------------
        # for index1 in range(0, len(nums)):
        #     for index2 in range(index1 + 1, len(nums)):
        #         if nums[index1] + nums[index2] == target:
        #             return [index1, index2]
        #  Method 1 -------------------------------------

        d = {}
        for index in range(0, len(nums)):
            if nums[index] in d:
                return sorted([index, d[nums[index]]])
            else:
                d[target - nums[index]] = index


def main():
    test = Solution()
    print test.twoSum([3, 2, 4], 6)
    print test.twoSum([1, 9, 2, 5, 3], 7)


main()