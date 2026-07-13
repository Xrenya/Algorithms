class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int out = 0;
        int min = prices[0];
        for (int i = 0; i < prices.size(); i++){
            if (min > prices[i]){
                min = prices[i];
            }
            else{
                int d = prices[i] - min;
                if (out < d){
                    out = d;
                }
            }
        }
        return out;
    }


    int maxProfitV2(vector<int>& prices) {
        int max = 0;
        int buy = prices[0];
        for (int i = 1; i < prices.size(); ++i) {
            int sell = prices[i];
            if (sell > buy) {
                max = std::max(max, sell - buy);
            } else {
                buy = sell;
            }
        }
        return max;
    }
};
