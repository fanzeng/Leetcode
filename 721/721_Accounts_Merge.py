class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        self.d_id_email = {}
        self.d_email_id = {}
        id = 0
        for account in accounts:
            name = account[0]
            emails = account[1:]
            # print name, emails
            person_ids = set()
            person_id = None
            for email in emails:
                if self.d_email_id.get(email) is not None:
                    person_ids.add(self.d_email_id[email])
                    if person_id is None:
                        person_id = self.d_email_id[email]
            if len(person_ids) == 0:
                # print 'new person', id, account
                person_id = id
                id += 1
                self.d_id_email[person_id] = [name, set()]
            for email in emails:
                self.d_id_email[person_id][1].add(email)
                self.d_email_id[email] = person_id
            # print person_ids
            self.merge(list(person_ids))
        # print self.d_email_id
        # print self.d_id_email
        return [[pair[0]] + sorted(list(pair[1])) for pair in self.d_id_email.values()]

    def merge(self, person_ids):
        if len(person_ids) < 2:
            return
        id = person_ids[0]
        for person_id in person_ids[1:]:
            emails = self.d_id_email[person_id][1]
            for email in emails:
                self.d_email_id[email] = id
                self.d_id_email[id][1].add(email)
            self.d_id_email.pop(person_id)
        # print self.d_email_id
        # print self.d_id_email
        # print 'merged persons', person_ids

test = Solution()
print test.accountsMerge(
    [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
)
print test.accountsMerge(
    [["Ethan","Ethan1@m.co","Ethan2@m.co","Ethan0@m.co"],["David","David1@m.co","David2@m.co","David0@m.co"],["Lily","Lily0@m.co","Lily0@m.co","Lily4@m.co"],["Gabe","Gabe1@m.co","Gabe4@m.co","Gabe0@m.co"],["Ethan","Ethan2@m.co","Ethan1@m.co","Ethan0@m.co"]]
)
print test.accountsMerge(
    [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
)