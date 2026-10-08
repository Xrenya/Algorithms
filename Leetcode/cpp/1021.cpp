#define pb push_back
#define pop pop_back

class Solution {
public:
    std::string removeOuterParentheses(std::string s) {
        std::vector<char> stack;
        std::string output;
        for (auto c : s) {
            if (c == ')') {
                stack.pop();
            }
            if (!stack.empty()) {
                output += c;
            }
            if (c == '(') {
                stack.pb(c);
            }
        }
        return output;
    }
};
