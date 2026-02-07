#include <iostream>
#include <string>
#include <vector>

class Solution {
public:
    int minimumDeletions(string s) {
        int size = s.size();
        std::vector<int> count_a(size, 0), count_b(size, 0);

        int b_count = 0;
        for (int i = 0; i < size; ++i) {
            count_b[i] = b_count;
            if (s[i] == 'b') {
                ++b_count;
            }
        }

        int a_count = 0;
        for (int i = size - 1; i >= 0; --i) {
            count_a[i] = a_count;
            if (s[i] == 'a') {
                ++a_count;
            }
        }
        int min_deletion = size;
        for (int i = 0; i < size; ++i) {
            min_deletion = std::min(min_deletion, count_a[i] + count_b[i]);
        }
        return min_deletion;
    }
};
