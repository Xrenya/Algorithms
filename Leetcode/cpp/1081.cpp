class Solution {
public:
    string smallestSubsequence(string s) {
        std::vector<int> last_index(26, 0);
        for (int i = 0; i < s.length(); ++i) {
            last_index[s[i] - 'a'] = i;
        }

        std::vector<bool> seen(26, false);
        std::string output;

        for (int i = 0; i < s.length(); ++i) {
            char chr = s[i];

            if (seen[chr - 'a']) {
                continue;
            }

            while (!output.empty() && output.back() > chr && last_index[output.back() - 'a'] > i) {
                seen[output.back() - 'a'] = false;
                output.pop_back();
            }
            seen[chr - 'a'] = true;
            output.push_back(chr);
        }

        return output;
    }
};
