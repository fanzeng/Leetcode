class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        # general idea:
        # convert bucket number into binary
        # assign pigs to each bit, for any bucket, if the bit of binary bucket number is 1, pig drinks the bucket
        # the death pattern of pig indicates the poisonous bucket.
        # the above strategy will find it out in one test period

        # now if you can do it in more test period
        # we can reduce the usage of pigs by using a larger base for the encoding
        # the key here is to use a base == the allowed number of test periods + 1
        # for test period number in range(0, total number of test_periods)
        # each pig, representing a bit, only drinks those buckets for which its bit == the test period number
        # then again, the death pattern of the pigs spells out the number for you
        import math
        period = minutesToTest / minutesToDie
        return int(math.ceil(math.log(buckets, period+1)))
