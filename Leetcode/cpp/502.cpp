class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        int n = profits.size();
        std::vector<std::pair<int, int>> projects(n);

        for (int i = 0; i < n; ++i) {
            projects[i] = {capital[i], profits[i]};
        }

        std::sort(projects.begin(), projects.end());

        std::priority_queue<int> maxProfitPq;
        int i = 0;

        while (k > 0) {
            while (i < n && projects[i].first <= w) {
                maxProfitPq.push(projects[i++].second);
            }
            if (maxProfitPq.empty()) {
                break;
            }
            w += maxProfitPq.top();
            maxProfitPq.pop();

            --k;
        }
        return w;
    }
};
