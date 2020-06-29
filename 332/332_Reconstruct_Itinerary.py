class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.tickets = sorted(tickets)
        self.used_tickets = []
        self.itinerary = ['JFK']
        self.constructItinerary()
        return self.itinerary

    def constructItinerary(self):
        airport = self.itinerary[-1]
        ticket_ids = self.getTicketFromAirport(airport)
        if ticket_ids is None or len(ticket_ids) == 0:
            return len(self.used_tickets) == len(self.tickets)
        while len(ticket_ids) > 0:
            ticket_id = ticket_ids.pop(0)
            ticket = self.tickets[ticket_id]
            airport = ticket[1]
            self.itinerary.append(airport)
            self.used_tickets.append(ticket_id)
            success = self.constructItinerary()
            if success:
                return True
            else:
                self.itinerary.pop()
                self.used_tickets.pop()

    def getTicketFromAirport(self, airport):
        ticket_ids = []
        for i, t in enumerate(self.tickets):
            if i not in self.used_tickets and t[0] == airport:
                ticket_ids.append(i)
        return ticket_ids

test = Solution()
print test.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]) # ["JFK", "MUC", "LHR", "SFO", "SJC"]
print test.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]) # ["JFK","ATL","JFK","SFO","ATL","SFO"]
print test.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])  # ["JFK","NRT","JFK","KUL"]
print test.findItinerary([["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]) # ["JFK","ANU","EZE","AXA","TIA","ANU","JFK","TIA","ANU","TIA","JFK"]