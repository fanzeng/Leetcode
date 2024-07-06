from collections import deque

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dirs = path.split('/')
        q = deque()
        for dir in dirs:
            if dir == '.':
                continue
            elif dir == '..':
                if len(q) > 0:
                    q.pop()
            else:
                dir.strip('/')
                if len(dir) > 0:
                    q.append(dir)
        return '/' + '/'.join(q) if len(q) > 0 else '/'
