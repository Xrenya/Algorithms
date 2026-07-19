class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};
        std::vector<std::string> output;
        std::vector<std::string> letters = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        std::function<void(std::string&, int)> dfs = [&](std::string& cur, int index) -> void {
            if (digits.size() == index) {
                output.push_back(cur);
                return;
            }
            for (const auto& letter : letters[digits[index] - '2']) {
                cur.push_back(letter);
                dfs(cur, index + 1);
                cur.pop_back();
            }
        };
        std::string tmp = "";
        dfs(tmp, 0);
        return output;
    }
};
