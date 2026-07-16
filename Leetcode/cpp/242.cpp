class SolutionV2 {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        std::sort(s.begin(), s.end());
        std::sort(t.begin(), t.end());
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] != t[i]) return false;
        }
        return true;
    }
};

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        std::vector<int> map(26, 0);
        for (int i = 0; i < t.length(); i++) {
            map[s[i] - 'a']++;
            map[t[i] - 'a']--;
        }
        for (int i = 0; i < 26; i++) {
            if (map[i] != 0) {
                return false;
            }
        }
        return true;
    }
};
