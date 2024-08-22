class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        self.d = {}
        self.piles = piles
        _, _, res = self.take(0, 1)
        return res

    # p: The starting index in the original pile for this turn
    # M: As defined in the question
    # returns: new p, new M, and the max number of stones starting from p
    def take(self, p, M):
        piles = self.piles[p:]
        if len(piles) <= 2*M:
            return len(self.piles), -1, sum(piles) # set M to -1 to end the game
        if self.d.get((p, M)) is not None:
            return self.d[(p, M)]
        res = 0
        taken = -1
        r = -1
        for i in range(1, 2*M+1):
            r = sum(piles[:i]) # immediate reward in this turn
            future = 0
            next_p, next_M, _ = self.take(p+i, max(M, i)) # opponent action
            if M > 0:
                _, _, future = self.take(next_p, next_M) # future rewards
                if r + future > res:
                    taken = i
                    res = r + future
        self.d[(p, M)] = p+taken, max(M, taken), res
        return self.d[(p, M)]
