class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        srcs = [src for (src, dst) in paths]
        dsts = [dst for (src, dst) in paths]
        for dst in dsts:
            if dst not in srcs:
                return dst
