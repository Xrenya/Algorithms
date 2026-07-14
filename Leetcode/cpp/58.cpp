class Solution {
public:
    int lengthOfLastWord(string s) {
        int maxLength = 0;
        bool letter = false;
        for (int i = s.length() - 1; i >= 0; --i) {
            if (!letter && s[i] == ' ') continue;
            if (letter && s[i] == ' ') break;
            if (s[i] != ' ') {
                letter = true;
            }
            ++maxLength;
        }
        return maxLength;
    }
};
