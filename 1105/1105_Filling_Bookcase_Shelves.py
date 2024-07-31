class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        self.w = shelfWidth
        self.d = {}
        return self.place(books, 0, 0)

    # max_h: Maximum height of current row
    # w: Consumed width
    def place(self, books, max_h, w):
        if len(books) == 0:
            return max_h
        key = len(books)
        if w == 0 and self.d.get(key) is not None:
            return self.d[key]
        t, h = books[0]
        if w > 0: # always place on same row if row is empty, so calc next_row only when row is nonempty
            next_row = self.place(books, 0, 0)
        if self.w - w < t: # not enough remaining space, have to place on next_row
            return max_h + next_row
        same_row = self.place(books[1:], max(max_h, h), w + t)
        if w == 0: # cache result of total height when starting new row from a book
            self.d[key] = same_row
            return same_row # since it's a new row, always place on the same_row.
        res = min(max_h + next_row, same_row)
        return res
