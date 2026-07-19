class Solution {
public:
    vector<string> generateParenthesis(int n) {
        std::vector<std::string> output;
        std::function<void(std::string&, int, int)> dfs = [&](std::string& tmp, int open, int close) -> void {
            if (open + close == 2 * n) {
                output.push_back(tmp);
                return;
            }
            if (open < n) {
                tmp.push_back('(');
                dfs(tmp, open + 1, close);
                tmp.pop_back();
            }
            if (open > close) {
                tmp.push_back(')');
                dfs(tmp, open, close + 1);
                tmp.pop_back();
            }
        };
        std::string tmp;
        dfs(tmp, 0, 0);
        return output;
    }
};
