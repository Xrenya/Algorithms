class Solution {
public:
    std::vector<int> buildLPS(const std::string& needle) {
        int n = needle.length();
        std::vector<int> prefix(n, 0);
        int index = 1;
        int length = 0;
        while (index < n) {
            if (needle[index] == needle[length]) {
                prefix[index++] = ++length;
            } else {
                if (length != 0) {
                    length = prefix[length - 1];
                } else {
                    prefix[index++] = 0;
                }
            }
        }
        return prefix;
    }

    int strStr(std::string haystack, std::string needle) {
        std::vector<int> lps = buildLPS(needle);
        int i = 0;
        int n = haystack.length();
        int m = needle.length();
        int j = 0;
        while (i < n) {
            if (haystack[i] == needle[j]) {
                ++i;
                ++j;

                if (j == m) {
                    return i - j;
                }
            } else {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    ++i;
                }
            }
        }
        return -1;
    }
};

class SolutionNotOptimal {
public:
    int strStr(string haystack, string needle) {
        int m = needle.length();
        int n = haystack.length();

        for (int windowStart = 0; windowStart <= n - m; windowStart++) {
            for (int i = 0; i < m; i++) {
                if (needle[i] != haystack[windowStart + i]) {
                    break;
                }
                if (i == m - 1) {
                    return windowStart;
                }
            }
        }

        return -1;
    }
};
