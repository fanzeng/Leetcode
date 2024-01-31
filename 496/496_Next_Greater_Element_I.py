class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        answer = [-1]*len(nums1)
        d = {}
        for i, n in enumerate(nums2):
            d[n] = i
        for i, n in enumerate(nums1):
            p = d[n]
            g = [v for k, v in d.items() if k > n and v > d[n]]
            if len(g) > 0:
                answer[i] = nums2[min(g)]
        return answer
