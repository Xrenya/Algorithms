class Solution {
public:
    int maximumLengthSubstring(string s) {
        std::unordered_map<char, int> map;
        int left = 0;
        int max_len = 0;
        for (int right = 0; right < s.length(); ++right) {
            char c = s[right];
            ++map[c];
            while (map[c] > 2) {
                char remove = s[left];
                --map[remove];
                ++left;
            }
            max_len = std::max<int>(max_len, right - left + 1);
        }
        return max_len;
    }
};
