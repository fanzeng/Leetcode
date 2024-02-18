import heapq

class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        self.n = n
        self.meetings = sorted(meetings, key=lambda m: m[0])
        self.count = [0]*n
        self.occupied_rooms = [] # priority queue, priority key is free_until
        self.free_rooms = [] # priority queue, priority key is room id

        for i in range(0, n):
            heapq.heappush(self.free_rooms, (i, i))
        t = 0
        for m in self.meetings:
            t = max(t, m[0])
            self.update_queues(t)
            if len(self.free_rooms) == 0: # have to wait for an occupied room
                earliest_occupied_avail = self.occupied_rooms[0][0]
                t = earliest_occupied_avail
                self.arrange(t, m)
            else: # take a free room to start m immediately
                t = max(t, m[0])
                self.arrange(t, m)
        print self.count
        return max([(i, c) for i, c in enumerate(self.count)], key=lambda x: x[1])[0]
    
    def arrange(self, t, m): # t is the earliest time when at least 1 room is free
        self.update_queues(t)
        _, i = heapq.heappop(self.free_rooms) # pop the first free room
        # print 't =', t, 'starting meeting', m[0], 'in room', i # use start time as id of meeting since they're unique
        self.count[i] += 1 # increase meeting room count
        free_until = t + m[1] - m[0]
        heapq.heappush(self.occupied_rooms, (free_until, i))
    
    def update_queues(self, t):
        # move all previously-occupied rooms that are free at t to the free-room queue
        while len(self.occupied_rooms) > 0 and self.occupied_rooms[0][0] <= t: # this room is free now, move it to self.free_rooms
            _, j = heapq.heappop(self.occupied_rooms)
            heapq.heappush(self.free_rooms, (j, j))
