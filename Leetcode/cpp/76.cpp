class Solution {
public:
    string minWindow(string s, string t) {
        if (s.empty() || t.empty() || s.length() < t.length()) {
            return "";
        }
        std::unordered_map<char, int> targetCounts, windowCount;
        for (auto chr : t) {
            ++targetCounts[chr];
        }

        int need = targetCounts.size();
        int have = 0;

        int minLen = INT_MAX;
        int startIndex = 0;
        int left = 0;
        for (int right = 0; right < s.length(); ++right) {
            char r_char = s[right];
            ++windowCount[r_char];

            if (targetCounts.contains(r_char) && windowCount[r_char] == targetCounts[r_char]) {
                ++have;
            }

            while (have == need) {
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    startIndex = left;
                }

                char l_char = s[left];
                --windowCount[l_char];

                if (targetCounts.contains(l_char) && windowCount[l_char] < targetCounts[l_char]) {
                    --have;
                }
                ++left;
            }
        }
        return minLen == INT_MAX ? "" : s.substr(startIndex, minLen);
    }
};
