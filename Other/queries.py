# Given the timestamps, action (not important what kind of activity it is) for each user
# write a class that would be able to get the number of users who had more than 1000 actions in the last 5 minutes
# ==========================================================
#    1 1 1 1 2 2 3 4 13 13          
#              |===============|
#                5 min window from the requested timestamp (get active users at ammortized comlexity O(1))
from collections import defaultdict, deque


class UsersActivity:
    def __init__(self):
        self.num_active_user = 0
        self.user_act_counter = defaultdict(int)  # {"user_id": activity counter}
        self.queue = deque([])  # [(timestamp (sec), user_id)]

    def insert(self, timestamp, user_id):
        self.user_act_counter[user_id] += 1
        self.queue.append((timestamp, user_id))
        if self.user_act_counter[user_id] == 1000:
            self.num_active_user += 1
        self.remove(timestamp)

    def remove(self, timestamp):
        while self.queue and timestamp - self.queue[0][0] > 5 * 60:  # 5 min into seconds
            _, user_id = self.queue.popleft()
            if self.user_act_counter[user_id] == 1000:
                self.num_active_user -= 1
            self.user_act_counter[user_id] -= 1
            # clean space from inactive users
            if self.user_act_counter[user_id] == 0:
                self.user_act_counter.pop(user_id)

    def request(self, timestamp):
        # The queue should be clean since request might come later than 5 min after the last activity
        # Improvements: it is possible to trigger the request in case it was not request awhile but 
        # our `queue` is still contains a lot of activity which is might be outdated since we need only 
        # the most active user_id  
        self.remove(timestamp)
        return self.num_active_user
