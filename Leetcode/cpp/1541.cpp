class Solution {
public:
    int minInsertions(string s) {
        int n = s.length();
        int insert = 0;
        int index = 0;
        int left = 0;
        while (index < n) {
            if (s[index] == '(') {
                ++left;
                ++index;
            } else {
                if (left > 0) {
                    --left;
                } else {
                    ++insert;
                }
                if (index < n - 1 && s[index + 1] == ')') {
                    index += 2;
                } else {
                    ++index;
                    ++insert;
                }
            }
        }
        insert += left * 2;
        return insert;
    }
};
