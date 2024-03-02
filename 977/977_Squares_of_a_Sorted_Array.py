class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums[0]**2]
        if nums[0] >= 0:
            return [n**2 for n in nums]
        if nums[-1] <= 0:
            return [n**2 for n in nums[::-1]]            
        res = []
        idx = 0
        while nums[idx] < 0:
            idx += 1
        p = idx
        n = idx - 1
        while p < len(nums) or n >= 0:
            if p < len(nums) and n >= 0:
                if abs(nums[n]) > nums[p]:
                    res.append(nums[p]**2)
                    p += 1
                else:
                    res.append(nums[n]**2)
                    n -= 1  
                continue  
            if p >= len(nums):
                res.append(nums[n]**2)
                n -= 1
                continue
            if n < 0:
                res.append(nums[p]**2)
                p += 1
        return res
