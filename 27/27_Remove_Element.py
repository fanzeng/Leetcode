class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] == val:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1
        # print nums
        # print "i =", i
        return i

def main():
    # nums = [3, 2, 2, 3]
    # val = 3
    nums = [3, 2, 3, 2, 2, 3, 2, 3]
    val = 3
    test = Solution()
    test.removeElement(nums, val)

main()