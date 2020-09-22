class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        self.trips = sorted(trips, key=lambda x: x[1])
        car_pos = 0
        car_cap = capacity
        l_trip = []
        for trip in self.trips:
            # print trip, car_pos, car_cap, l_trip
            n = trip[0]
            start = trip[1]
            end = trip[0]
            car_pos = start
            l_trip_new = []
            for t in l_trip:
                if t[2] <= car_pos:
                    car_cap += t[0]
                else:
                    l_trip_new.append(t)
            l_trip = l_trip_new
            if car_cap < n:
                return False
            car_cap -= n
            l_trip.append(trip)
        return True

test = Solution()
print test.carPooling([[2,1,5],[3,3,7]], 4) # False
print test.carPooling([[2,1,5],[3,3,7]], 5) # True
print test.carPooling([[2,1,5],[3,5,7]], 3) # True
print test.carPooling([[3,2,7],[3,7,9],[8,3,9]], 11) # True