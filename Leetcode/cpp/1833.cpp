class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        std::sort(costs.begin(), costs.end());
        int counter = 0;
        for (auto c : costs) {
            if (c <= coins) {
                coins -= c;
                ++counter;
            } else {
                break;
            }
        }
        return counter;   
    }
};
