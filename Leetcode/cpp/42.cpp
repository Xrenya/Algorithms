class Solution {
public:
    int trap(vector<int>& height) {
        std::vector<std::pair<int, int>> stack;
        int output = 0;
        for (int i = 0; i < height.size(); ++i) {
            if (stack.empty() || stack.back().second > height[i]) {
                stack.push_back({i, height[i]});
            } else {
                while (!stack.empty() && stack.back().second < height[i]) {
                    int bottom_height = stack.back().second;
                    stack.pop_back();
                    
                    if (stack.empty()) {
                       break;
                    }
                    int left_index = stack.back().first;
                    int left_height = stack.back().second;
                    
                    int distance = i - left_index - 1;
                    int bounded_height = std::min(left_height, height[i]) - bottom_height;
                    output += distance * bounded_height;
                }
                stack.push_back({i, height[i]});
            }
        }

        return output;
    }
};
