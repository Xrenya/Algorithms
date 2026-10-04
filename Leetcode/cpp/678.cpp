#define pb push_back
#define pp pop_back


class Solution {
public:
    bool checkValidString(string s) {
        std::vector<int> open;
        std::vector<int> ast;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == '(') {
                open.pb(i);
            } else if (s[i] == '*') {
                ast.pb(i);
            } else {
                if (!open.empty()) {
                    open.pp();
                } else if (!ast.empty()) {
                    ast.pp();
                } else {
                    return false;
                }
            }
        }
        while (!open.empty() && !ast.empty()) {
            if (open.back() > ast.back()) {
                return false;
            }
            open.pop_back();
            ast.pop_back();
        }
        return open.empty();
    }
};
