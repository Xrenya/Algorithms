class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        std::unordered_map<char, char> s2t, t2s;

        for (int i = 0; i < s.length(); ++i) {
            char sChar = s[i];
            char tChar = t[i];
            if (!s2t.contains(sChar) && !t2s.contains(tChar)) {
                s2t[sChar] = tChar;
                t2s[tChar] = sChar;
            } else if ((!s2t.contains(sChar) && t2s.contains(tChar)) || (s2t.contains(sChar) && !t2s.contains(tChar)) || (s2t[sChar] != tChar || t2s[tChar] != sChar)) {
                return false;
            }
        }
        return true;
    }
};
