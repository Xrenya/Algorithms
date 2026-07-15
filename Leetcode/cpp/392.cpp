class Solution {
public:
    bool isSubsequence(string s, string t) {
        int index = 0;
        for (int i = 0; i < t.size(); i++){
            if (index < s.size() and s[index] == t[i]){
                index++;
            }
        }
        return index == s.size();
    }
};


class SolutionV1 {
public:
    bool isSubsequence(string s, string t) {
        if (s.length() > t.length()) {
            return false;
        } else if (s.length() == t.length()) {
            return s == t;
        } else if (s.length() == 0) {
            return true;
        }
        int index = 0;
        for (int i = 0; i < t.length(); ++i) {
            if (s[index] == t[i]) {
                ++index;
            }
            if (index == s.length()) {
                return true;
            }
        }
        return false;
    }
};
