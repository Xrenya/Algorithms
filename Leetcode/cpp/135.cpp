class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        vector<int> output(n, 1);

        for (int i = 1; i < n; ++i) {
            if (ratings[i - 1] > ratings[i]) {
                output[i - 1] = std::max<int>(output[i - 1], output[i] + 1);
            } else if (ratings[i - 1] < ratings[i]) {
                output[i] = std::max<int>(output[i], output[i - 1] + 1);
            }
        }
        for (int i = n - 2; i >= 0; --i) {
            if (ratings[i + 1] > ratings[i]) {
                output[i + 1] = std::max<int>(output[i + 1], output[i] + 1);
            } else if (ratings[i + 1] < ratings[i]){
                output[i] = std::max<int>(output[i], output[i + 1] + 1);
            }
        }
        int sum = std::accumulate(output.begin(), output.end(), 0);
        return sum;
    }
};
