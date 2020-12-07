class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        return self.asteroidCollisionRecursive(asteroids)

    def asteroidCollisionRecursive(self, asteroids):
        remain_asteroids = self.collide(asteroids)
        # print remain_asteroids
        if len(remain_asteroids) == len(asteroids):
            return asteroids
        else:
            return self.asteroidCollisionRecursive(remain_asteroids)

    def collide(self, asteroids):
        if len(asteroids) < 2:
            return asteroids
        remain_asteroids = []
        collided = False
        for i in xrange(1, len(asteroids)):
            a = asteroids[i-1]
            b = asteroids[i]
            if a > 0 and b < 0:
                collided = True
                if abs(a) == abs(b):
                    continue
                else:
                    new_asteroid = max(abs(a), abs(b))
                    if abs(a) < abs(b):
                        new_asteroid *= -1
                    remain_asteroids.append(new_asteroid)
            else:
                if not collided:
                    remain_asteroids.append(asteroids[i-1])
                collided = False
        if not collided:
            remain_asteroids.append(asteroids[-1])
        return remain_asteroids


test = Solution()
print test.asteroidCollision([5,10,-5]) # [5,10]
print test.asteroidCollision([8,-8]) # []
print test.asteroidCollision([10,2,-5]) # [10]
print test.asteroidCollision([-2,-1,1,2]) # [-2,-1,1,2]
print test.asteroidCollision([-2,1,-2,-2]) # [-2,-2,-2]