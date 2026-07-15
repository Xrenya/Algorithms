class Solution {
public:
    int skipSpaces(int index, std::string& line) {
        while (index >= 0 && line[index] == ' ') {
            --index;
        }
        return index;
    }

    int findBeginingOfWord(int index, std::string& line) {
        while (index >= 0 && line[index] != ' ') {
            --index;
        }
        return index;
    }
    string reverseWords(string s) {
        if (s.length() <= 1) {
            return s;
        }
        int n = s.length();
        int left = n - 1;
        int right = n - 1;
        std::string output;
        while (right > 0) {
            left = skipSpaces(left, s);
            right = left;
            left = findBeginingOfWord(left, s) + 1;
            if (left <= right && output.size() > 0) {
                output += " ";
            }
            int reset = left - 1;
            while (left <= right) {
                output += s[left++];
            }
            left = reset;
            right = reset;
        }
        return output;
    }
};
