class Solution {
public:
    int hIndex(vector<int>& citations) {
        std::sort(citations.begin(), citations.end(),
            [](int a, int b) {
                if (a > b) {
                    return true;
                }
                return false;
            }
        );
        for (int i = 0; i < citations.size(); ++i) {
            if (i >= citations[i]) {
                return i;
            }
        }
        return citations.size();

    }
};
