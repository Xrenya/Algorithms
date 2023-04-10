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
