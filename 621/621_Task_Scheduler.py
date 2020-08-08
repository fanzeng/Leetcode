class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        self.n = n
        self.d = {}
        self.d_task_count = {}
        for t in tasks:
            if t in self.d_task_count:
                self.d_task_count[t] += 1
            else:
                self.d_task_count[t] = 1
        self.num_task_types = len(self.d_task_count.keys())
        self.l_task_count = sorted(self.d_task_count.values(), reverse=True)
        if self.n >= self.num_task_types: # if we have to cooldown for more than the number of task types, then there is no better way than just do alphabetic order and cycle, the job with max count will determine the number of cycles.
            time = (self.l_task_count[0]-1)*(1+self.n) + 1
            for i, task in enumerate(self.l_task_count[1:]):
                if self.l_task_count[0] == task:
                    time += 1
                else:
                    break
            return time

        if self.n == 0:
            return sum(self.l_task_count)

        if max(self.l_task_count) == min(self.l_task_count): # special case, when the task number distribution is uniform
            s = ''
            for i in xrange(self.l_task_count[0]):
                for j in xrange(self.num_task_types):
                    s += str(unichr(ord('A') + j))
            return self.strToTime(s)

        # case when self.n is less than self.num_task_type, this is the most complicated one
        # in this case, prefer to even out the differences among tasks
        # to do so, at any time, choose the task that is both valid (meaning no need to cool down, when possible of course)
        # and has the maximum remaining number
        l_task_count = self.l_task_count[:]
        s = 'A'
        l_task_count[0] -= 1
        while max(l_task_count) > 0:
            options = [i for i in xrange(self.num_task_types) if l_task_count[i] > 0]
            for c in s[-min(len(s), self.n):][::-1]: # when we have to wait for cool down, prefer to do next the task that has been done least recently, thus, remove options in reverse order
                invalid_option = ord(c) - (ord('A'))
                if invalid_option in options and len(options) > 1:
                    options.remove(invalid_option)
            option = options[self.argmax([l_task_count[i] for i in options])]
            s += str(unichr(ord('A') + option))
            l_task_count[option] -= 1
        return self.strToTime(s)

    def strToTime(self, s):
        time = 0
        l_cool = [0]*26
        for c in s:
            remain = l_cool[ord(c) - ord('A')]
            delta_time = 1
            if remain > 0:
                delta_time += remain
            l_cool = [cool - delta_time if cool > delta_time else 0 for cool in l_cool]
            time += delta_time
            l_cool[ord(c)-ord('A')] = self.n
        return time

    def argmax(self, l):
        return sorted(zip(xrange(len(l)), l), reverse=True, key=lambda x:x[1])[0][0]

test = Solution()
print test.leastInterval(["A","B","A"], 2) # 4
print test.leastInterval(["A","A","A","B","B","B"], 2) # 8
print test.leastInterval(["A","A","A","B","B","B"], 0) # 6
print test.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2) # 16
print test.leastInterval(["A","B","C","D","E","F","A","B","C","D","E","F"], 2) # 12

print test.leastInterval(
["A","A","B","B","C","C","D","D","E","E","F","F","G","G","H","H","I","I","J","J","K","K","L","L","M","M","N","N","O","O","P","P","Q","Q","R","R","S","S","T","T","U","U","V","V","W","W","X","X","Y","Y","Z","Z"],
2) # 52

print test.leastInterval(
["B","F","J","J","H","A","D","C","C","D","J","E","B","E","C","H","E","E","G","E","H","I","I","E","H","F","C","G","H","F","E","E","I","D","D","A","E","A","C","E","F","J","E","F","G","J","A","A","A","B","E","J","H","C","A","E","D","A","E","I","H","B","A","C","E","F","J","D","F","I","I","H","J","E","B","H","H","A","J","C","C","D","C","B","C","H","H","I","H","D","C","B","D","C","H","A","F","A","J","D","F","E","H","I","D","A","E","B","H","J","F","D","C","J","J","I","A","I","J","H","A","I","I","G","C","C","H","D","B","B","B","H","I","D","B","C","H","I","I","G","E","D","D","A","E","D","H","C","J","H","C","E","I","F","A","I","E","G","A","E","F","I","B","J","B","J","B","G","A","D","C","B","I","A","C","J","J","J","B","E","E","E","B","E","B","H","B","J","H","F","G","B","B","I","C","D","I","D","D","A","I","D","H","A","J","D","J","D","I","G","F","F","B","G","A","F","I","I","H","C","B","H","H","E","F","A","H","G","F","D","G","F","A","C","F","D","F","C","J","A","D","H","G","D","D","G","C","G","C","I","B","G","E","J","C","G","J","G","E","F","F","I","D","D","E","G","F","A","F","H","D","C","B","E","H","G","H","B","A","D","A","J","A","C","B","G","C","A","J","E","I","G","H","J","A","J","I","D","I","G","B","G","I","A","B","J","B","H","E","G","G","I","G","G","C","J","J","J","H","G","A","G","B","G","I","G","A","D","B","A","E","I","H","E","G","H","J","F","H","I","A","E","A","I","A","D","D","B","D","G","E","C","J","C","C","B","F","F","B","E","A","G","D","I","G","D","J","D","G","I","B","J","J","B","F","D","I","C","I","B","J","B","D","D","A","D","C","G","A","G","C","G","C","E","C","G","A","J","C","E","F","C","C","E","J","D","H","H","F","E","D","G","E","E","I","B","G","A","C","C","E","J","F","H","C","A","G","H","G","A","G","A","D","B","E","F","H","C","C","B","I","F","H","I","C","H","G","G","C","E","A","J","F","F","F","B","D","I","E","I","F","E","F","G","G","A","D","I","A","J","A","H","J","I","H","H","A","B","B","B","I","C","J","C","G","J","G","E","I","H","D","E","H","J","A","G","A","G","A","C","F","C","G","E","G","J","D","H","H","B","J","F","J","J","B","J","D","D","G","B","I","I","H","G","B","I","E","D","H","H","I","B","A","A","A","D","H","J","H","D","J","E","D","G","J","B","B","F","G","J","G","E","G","E","E","F","H","F","J","A","G","I","D","C","H","A","C","F","B","J","E","I","A","G","J","D","I","F","I","J","H","E","D","J","A","E","G","B","B","J","I","J","H","F","D","F","F","A","G","F","F","I","C","H","E","E","G","A","D","F","I","D","D","C","B","G","C","D","G","H","F","D","J","D","B","A","J","J","I","H","F","G","D","J","H","I","H","I","A","A","I","C","B","H","G","I","C","F","E","J","J","F","F","D","F","A","J","H","B","G","A","F","D","G","D","C","F","J","F","G","D","H","J","C","A","E","C","G","J","G","I","C","G","H","G","J","D","D","G","D","F","F","J","B","D","C","E","F","G","D","A","J","H","D","F","C","B","H","C","I","D","C","F","E","C","D","J","D","E","G","C","D","H","J","E","H","I","I","A","C","E","C","I","B","A","B","E","E","H","E","B","H","C","G","B","C","C","D","G","G","A","F","A","B","D","G","F","A","H","G","C","E","D","B","H","D","F","F","G","A","J","H","E","B","C","B","B","B","H","D","F","B","B","C","G","A","C","E","J","H","F","F","D","G","J","D","F","J","G","H","B","D","B","D","D","G","J","H","B","D","F","E","E","G","D","H","B","A","I","E","B","E","B","D","I","C","A","A","E","J","A","B","A","F","C","J","F","F","F","A","I","J","F","H","G","C","F","E","D","C","B","C","G","G","G","A","B","J","J","F","J","G","C","D","B","C","F","H","I","F","D","C","I","J","D","I","G","B","G","I","J","E","H","G","G","J","J","A","E","E","I","G","E","H","F","F","C","A","J","I","I","D","C","E","G","A","A","H","F","A","I","B","H","J","H","B","H","A","A","A","G","I","I","D","F","F","C","H","D","B","J","F","G","E","F","J","A","I","G","J","J","F","F","G","B","B","D","F","E","G","D","D","A","D","D","G","C","C","I","C","H","I","C","E","G","C","E","J","F","G","J","B","I","B","B","C","B","G","A","J","H","C","G","D","E","H","E","H","A","H","I","A","J","C","G","B","G","H","G","H"],
36) # 4256

print test.leastInterval(
["D","C","G","I","F","J","J","G","J","E","A","F","C","E","I","B","G","E","A","D","E","E","D","J","H","B","F","G","F","H","B","G","E","I","D","F","H","F","I","J","E","H","E","D","B","D","F","E","A","G","B","J","A","J","B","C","I","J","H","J","C","H","H","F","G","D","G","J","C","I","I","B","I","I","B","C","B","F","J","D","G","H","J","H","G","A","J","J","I","J","B","J","G","A","J","I","E","F","B","D","A","E","G","J","D","E","F","A","A","E","D","I","D","I","I","F","E","F","D","H","J","D","F","G","H","D","H","A","F","F","G","E","B","I","G","A","D","E","B","D","J","A","H","A","A","B","F","B","G","C","D","E","G","B","B","F","E","B","I","B","H","I","E","G","I","E","E","I","F","B","I","C","J","I","C","J","I","C","D","E","H","G","F","G","F","E","A","E","A","E","E","D","E","D","H","C","D","J","D","F","E","H","A","C","G","D","A","J","J","E","D","I","H","C","B","C","I","H","C","E","G","C","D","E","J","H","C","J","G","B","C","H","E","H","D","A","D","J","G","D","B","H","C","G","I","D","J","I","G","F","G","A","I","E","B","J","D","I","G","H","E","B","B","B","C","J","B","G","E","I","H","I","F","J","I","B","B","B","H","I","I","G","C","B","G","C","I","B","A","J","H","A","G","B","H","A","G","B","D","J","J","J","E","I","E","I","D","D","J","J","D","D","E","E","B","A","F","H","C","E","I","I","E","B","H","E","H","H","E","E","G","G","A","F","J","E","G","D","G","C","C","C","D","E","I","J","I","H","A","B","C","C","C","G","G","A","C","F","B","E","C","B","C","I","F","G","C","B","G","C","G","D","D","G","B","E","A","J","H","B","C","C","E","J","I","I","I","H","H","B","F","J","G","A","I","A","F","J","H","A","H","D","F","E","A","A","F","B","D","J","B","I","C","I","G","G","G","D","G","B","G","C","D","J","H","A","C","A","A","A","E","J","A","C","J","H","D","F","E","J","H","F","A","A","A","G","D","G","A","A","J","D","B","B","H","A","B","D","F","D","D","B","D","B","A","B","A","H","J","E","F","H","G","H","I","J","B","H","F","F","D","C","A","D","E","F","B","F","F","E","D","F","A","G","E","B","J","F","J","C","J","I","J","J","A","C","C","D","F","D","E","C","G","B","F","H","I","B","F","I","C","B","B","A","C","C","J","D","J","J","I","B","F","J","B","D","D","G","G","H","G","G","C","E","I","D","B","A","H","I","B","G","E","H","D","D","C","G","E","E","G","A","C","J","J","E","B","F","J","I","G","E","C","H","I","I","C","J","D","G","E","G","A","G","A","J","B","F","B","G","B","J","E","C","F","B","A","J","G","A","G","B","J","A","C","D","H","C","E","G","C","H","D","I","E","E","I","B","G","H","D","A","I","A","C","B","D","B","B","A","D","I","J","G","D","D","D","B","J","H","D","B","F","J","J","F","D","G","C","H","I","E","G","J","J","B","E","D","A","G","I","C","C","E","B","H","A","F","D","D","G","E","E","C","I","J","C","G","C","E","D","B","F","F","A","D","I","E","F","J","J","F","A","B","D","G","J","G","B","I","B","J","A","I","I","D","H","A","F","I","A","A","F","F","D","E","E","I","G","B","G","G","J","J","E","F","A","H","E","I","A","B","D","I","E","I","C","B","F","J","G","D","C","I","C","G","B","G","A","J","F","C","B","J","D","D","F","F","D","B","I","A","F","J","C","H","F","A","H","D","F","D","G","I","C","H","E","D","J","E","A","G","H","B","J","B","J","A","A","A","H","E","B","J","E","J","E","C","D","I","F","C","C","G","J","D","E","H","C","B","B","B","C","C","C","A","E","G","J","G","E","C","H","I","C","H","E","E","G","H","H","B","C","A","E","H","G","C","G","G","B","J","H","C","G","I","G","B","H","A","C","A","B","F","I","A","F","B","D","E","H","C","G","I","A","F","G","H","B","B","E","D","E","D","D","J","A","D","J","H","F","A","A","F","C","A","D","C","A","H","E","D","C","E","H","G","G","C","G","G","I","G","E","J","E","I","E","I","C","G","C","G","E","B","J","A","G","G","D","F","E","H","D","D","D","F","D","B","F","I","C","E","B","B","D","C","E","D","B","H","J","G","G","C","F","J","D","D","D","A","H","E","A","F","I","G","F","A","A","A","F","H","B","I","F","F","H","C","I","J","C","D","B","G","I","E","A","C","F","I","J","F","D","J","D","F","C","I","G","F","H","F","I","E","C","B","B","H","B","A"],
88) # 9793

print test.leastInterval(
["F","J","J","A","J","F","C","H","J","B","E","G","G","F","A","C","I","F","J","C","J","C","H","C","A","D","G","H","B","F","G","C","C","A","E","B","H","J","E","I","F","D","E","A","C","D","B","D","J","J","C","F","D","D","J","H","A","E","C","D","J","D","G","G","B","C","E","G","H","I","D","H","F","E","I","B","D","E","I","E","C","J","G","I","D","E","D","J","C","A","C","C","D","I","J","B","D","H","H","J","G","B","G","A","H","E","H","E","D","E","J","E","J","C","F","C","J","G","B","C","I","I","H","F","A","D","G","F","C","C","F","G","C","J","B","B","I","C","J","J","E","G","H","C","I","G","J","I","G","G","J","G","G","E","G","B","I","J","B","H","D","H","G","F","C","H","C","D","A","G","B","H","H","B","J","C","A","F","J","G","F","E","B","F","E","B","B","A","E","F","E","H","I","I","C","G","J","D","H","E","F","G","G","D","E","B","F","J","J","J","D","H","E","B","D","J","I","F","C","I","E","H","F","E","G","D","E","C","F","E","D","E","A","I","E","A","D","H","G","C","I","E","G","A","H","I","G","G","A","G","F","H","J","D","F","A","G","H","B","J","A","H","B","H","C","G","F","A","C","C","B","I","G","G","B","C","J","J","I","E","G","D","I","J","I","C","G","A","J","G","F","J","F","C","F","G","J","I","E","B","G","F","A","D","A","I","A","E","H","F","D","D","C","B","J","I","J","H","I","C","D","A","G","F","I","B","E","D","C","J","G","I","H","E","C","E","I","I","B","B","H","J","C","F","I","D","B","F","H","F","A","C","A","A","B","D","C","A","G","B","G","F","E","G","A","A","A","C","J","H","H","G","C","C","B","C","E","B","E","F","I","E","E","D","I","H","G","F","A","H","B","J","B","G","H","C","C","B","G","C","B","A","E","G","A","J","G","D","C","I","G","F","G","G","A","J","E","I","D","E","A","F","A","H","C","E","D","D","D","H","I","F","F","A","F","A","A","C","J","D","J","H","I","F","A","C","B","C","A","C","C","H","A","J","I","B","A","I","F","J","C","I","B","C","E","E","E","J","G","F","E","I","A","A","E","B","J","H","H","H","A","H","J","E","F","E","F","G","J","D","I","D","I","F","B","J","D","A","A","D","F","G","B","J","H","F","A","D","H","C","B","A","J","H","I","F","H","E","G","B","A","F","F","A","C","D","G","I","I","J","H","H","C","J","G","B","A","D","B","F","J","D","I","A","F","F","F","F","A","E","B","C","G","H","E","B","B","A","G","D","C","C","E","A","C","F","G","A","I","F","B","H","J","G","C","B","H","D","A","H","B","H","H","C","A","F","I","C","F","A","C","J","I","H","H","F","B","B","D","E","C","J","F","C","E","A","J","E","C","A","E","B","A","J","F","J","J","J","H","H","C","I","E","G","G","H","J","J","H","H","H","J","H","A","G","I","C","E","C","D","G","G","F","H","D","G","H","A","E","I","D","A","H","G","E","A","B","F","I","C","A","F","B","A","I","F","G","I","F","D","A","B","J","B","D","F","G","J","J","A","A","C","H","G","F","B","I","I","J","A","H","D","F","E","F","J","B","F","C","G","E","A","G","H","E","H","H","F","I","G","C","C","G","J","B","H","F","H","D","I","B","D","I","F","H","I","D","F","G","G","E","A","C","A","G","H","G","H","J","F","D","F","G","D","D","C","J","C","J","G","G","G","G","H","H","G","D","E","H","G","C","B","F","I","F","C","H","J","I","A","F","D","C","F","C","E","E","D","D","C","G","B","F","E","J","C","I","E","D","B","B","I","I","I","H","C","E","C","J","F","G","A","I","J","D","I","C","G","F","I","E","I","E","F","A","G","E","J","A","I","A","D","A","G","J","F","E","D","I","A","E","J","I","C","J","B","F","B","E","C","E","F","G","E","J","J","I","E","D","F","C","H","H","B","G","D","I","I","F","B","G","C","F","J","B","G","J","H","D","G","C","C","I","I","E","I","B","H","B","I","G","F","H","G","C","J","D","C","E","G","F","C","H","D","A","C","D","H","B","C","H","I","B","A","J","C","B","D","J","D","H","F","B","A","G","G","J","I","E","F","A","D","H","D","B","C","A","H","F","G","B","F","H","B","H","I","J","D","H","I","B","C","D","G","A","E","A","A","I","F","I","F","B","B","I","F","A","E","I","A","B","G","C","F","I","A","F","I","D","H","B","I","I","B","J","F","E","B","B","B","D","C","J","E","J","J","G","D","F","F","F","G","I","H","J","J","G","D","G","F"],
8) # 1000

print test.leastInterval(["A","A","A","B","B","B","C","D","E","F","G","H","I","J","K"], 7) # 18