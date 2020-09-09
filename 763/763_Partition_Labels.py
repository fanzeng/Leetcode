class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        self.res = []
        self.l_part_loc = []
        self.d_char = {}
        for i, char in enumerate(S):
            if self.d_char.get(char) is None:
                self.d_char[char] = [i]
            else:
                self.d_char[char].append(i)
        # print self.d_char

        i = 0
        while i < len(S):
            part_loc = self.d_char[S[i]][-1]
            j = i + 1
            while j < part_loc:
                char = S[j]
                last_occur = self.d_char[char][-1]
                j += 1
                part_loc = max(part_loc, last_occur)
            i = part_loc + 1
            # print i, 'part_loc', part_loc
            self.l_part_loc.append(part_loc)
        self.res.append(self.l_part_loc[0] + 1)
        for i in xrange(1, len(self.l_part_loc)):
            self.res.append(self.l_part_loc[i] - self.l_part_loc[i-1])
        return self.res

test = Solution()
print test.partitionLabels("ababcbacadefegdehijhklij") # [9,7,8]
