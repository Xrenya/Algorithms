class Solution {
public:
    int maxDepth(string s) {
        int counter = 0;
        int max = 0;
        for (const auto& c : s) {
            if (c == '(') {
                ++counter;
            } else if (c == ')') {
                --counter;
            }
            max = std::max<int>(max, counter);
        }
        return max;
    }
};
