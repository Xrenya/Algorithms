class Solution {
public:
    bool isValid(string s) {
        std::map<char, char> map = {{'(', ')'}, {'{', '}'}, {'[', ']'}};
        std::vector<char> query;
        for (auto c: s) {
          if (map.find(c) != map.end()) {
            query.push_back(map[c]);
          } else if (!query.empty() && query.back() == c) {
            query.pop_back();
          } else {
            return false;
          }
        }
      return query.empty() ? true : false;
    }
};

class SolutionV2 {
public:
    bool isValid(string s) {
        std::vector<char> stack;
        for (const auto& c : s) {
            if (c == '(') {
                stack.push_back(')');
            } else if (c == '[') {
                stack.push_back(']');
            } else if (c == '{') {
                stack.push_back('}');
            } else {
                if (!stack.empty() && stack.back() == c) {
                    stack.pop_back();
                    continue;
                } else {
                    return false;
                }
            }
        }
        return stack.empty();
    }
};
