class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        std::vector<int> total_days(*max_element(days.begin(), days.end()) + 1, 0);
        std::set<int> set_days(days.begin(), days.end());
        for (int day = 1; day < total_days.size(); day++) {
            if (set_days.find(day) != set_days.end()) {
                total_days[day] = std::min(std::min(total_days[std::max(day - 1, 0)] + costs[0], total_days[std::max(day - 7, 0)] + costs[1]), total_days[std::max(day - 30, 0)] + costs[2]);
            } else {
                total_days[day] = total_days[day - 1];
            }
        }
        return total_days[total_days.size() - 1];
    }
};
