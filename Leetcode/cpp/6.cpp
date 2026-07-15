class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows <= 1 || s.length() <= numRows) {
            return s;
        }

        std::string output;
        int length = s.length();
        int index = 0;
        for (int i = 0; i < numRows; ++i) {
            int dist = 2 * numRows - 2;
            int pos = i;
            int inBetweenOffset = dist - 2 * i;
            while (pos < length) {
                output += s[pos];
                if ((i != 0 && i != numRows - 1) && pos + inBetweenOffset < length) {
                    output += s[pos + inBetweenOffset];
                }
                pos += dist;
            }
        }

        return output;
    }
};
