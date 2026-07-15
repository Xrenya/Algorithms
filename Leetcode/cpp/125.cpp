class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.length() - 1;
        while (left <= right) {
            if (!std::isalnum(s[left])) {
                ++left;
            } else if (!std::isalnum(s[right])) {
                --right;
            } else {
                if (std::tolower(s[left]) != std::tolower(s[right])) {
                    return false;
                }
                ++left;
                --right;
            }
        }
        return true;
    }
};
