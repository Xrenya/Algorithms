class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::set<char> uset;
        int j = 0;
        int maxLen = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (!uset.contains(s[i])) {
                uset.insert(s[i]);
                maxLen = std::max<int>(maxLen, i - j + 1);
            } else {
                while (uset.contains(s[i])) {
                    uset.erase(s[j++]);
                }
                uset.insert(s[i]);
            }
        }
        return maxLen;
    }
};
