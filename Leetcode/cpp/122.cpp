class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int acc = 0;
        int buy = prices[0];
        for (int i = 1; i < prices.size(); ++i) {
            int sell = prices[i];
            if (sell > buy) {
                acc += (sell - buy);
            }
            buy = sell;
        }
        return acc;
    }
};
