class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        queue = []
        for a in asteroids:
            while queue and queue[-1] > 0 and queue[-1] > a and a < 0:
                if queue[-1] < -a:
                    queue.pop()
                    continue
                elif queue[-1] == -a:
                    queue.pop()
                break
            else:
                queue.append(a)
        return queue

                 
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        q = [asteroids[0]]
        for a in asteroids[1:]:
            if a > 0:
                q.append(a)
            else:
                idx = len(q) - 1
                remove = []
                destroyed = False
                while idx >= 0:
                    if q[idx] > 0 and q[idx] > abs(a):
                        destroyed = True
                        break
                    elif q[idx] > 0 and q[idx] < abs(a):
                        remove.append(idx)
                    elif q[idx] > 0 and q[idx] == abs(a):
                        destroyed = True
                        remove.append(idx)
                        break
                    idx -= 1
                if not destroyed:
                    q.append(a)
                if remove:
                    temp = []
                    idx = len(remove) - 1
                    for i in range(len(q)):
                        if idx < len(remove) and i == remove[idx]:
                            idx -= 1
                        else:
                            temp.append(q[i])
                    q = temp

        return q
