class UndergroundSystem(object):

    def __init__(self):
        self.dUser = {}
        self.dTravel = {}

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.dUser[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        startStation, tStart = self.dUser[id]
        h = self.getHash(startStation, stationName)
        if self.dTravel.get(h) is None:
            self.dTravel[h] = ((t - tStart)*1.0, 1)
        else:
            oldAvg, count = self.dTravel[h]
            newAvg = (oldAvg*count + (t - tStart))/(count + 1)
            self.dTravel[h] = (newAvg, count + 1)

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        h = self.getHash(startStation, endStation)
        return self.dTravel[h][0]

    def getHash(self, startStation, endStation):
        return startStation + ',' + endStation

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkIn(32, "Paradise", 8)
undergroundSystem.checkIn(27, "Leyton", 10)
undergroundSystem.checkOut(45, "Waterloo", 15)
undergroundSystem.checkOut(27, "Waterloo", 20)
undergroundSystem.checkOut(32, "Cambridge", 22)
print undergroundSystem.getAverageTime("Paradise", "Cambridge") # 14.00000
print undergroundSystem.getAverageTime("Leyton", "Waterloo") # 11.00000
undergroundSystem.checkIn(10, "Leyton", 24)
print undergroundSystem.getAverageTime("Leyton", "Waterloo") # 11.00000
undergroundSystem.checkOut(10, "Waterloo", 38)
print undergroundSystem.getAverageTime("Leyton", "Waterloo") # 12.00000

undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(10, "Leyton", 3)
undergroundSystem.checkOut(10, "Paradise", 8)
print undergroundSystem.getAverageTime("Leyton", "Paradise") # 5.00000
undergroundSystem.checkIn(5, "Leyton", 10)
undergroundSystem.checkOut(5, "Paradise", 16)
print undergroundSystem.getAverageTime("Leyton", "Paradise") # 5.50000
undergroundSystem.checkIn(2, "Leyton", 21)
undergroundSystem.checkOut(2, "Paradise", 30)
print undergroundSystem.getAverageTime("Leyton", "Paradise") # 6.66667