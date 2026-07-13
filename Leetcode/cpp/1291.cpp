class Solution {
public:
    void dfs(int digit, int low, int high, std::vector<int>& output) {
        if (digit > high) {
            return;
        }
        if (digit >= low) {
            output.push_back(digit);
        }
        int last = digit % 10 + 1;
        if (last <= 9) {
            dfs(digit * 10 + last, low, high, output);
        }
        return;
    }

    std::vector<int> sequentialDigits(int low, int high) {
        std::vector<int> output;
        
        for (int i = 1; i < 10; ++i) {
            dfs(i, low, high, output);
        }
        std::sort(output.begin(), output.end());
        return output;
    }

    std::vector<int> sequentialDigitsString(int low, int high) {
        std::string digits = "123456789";
        std::vector<int> output;
        for (int w = 2; w < 10; ++w) {
            for (int start = 0; start <= digits.size() - w; ++start) {
                std::string digit = digits.substr(start, w);
                int tmp = std::stoi(digit);

                if (tmp >= low && tmp <= high) {
                    output.push_back(tmp);
                }
            }
        }
        return output;
    }
};
