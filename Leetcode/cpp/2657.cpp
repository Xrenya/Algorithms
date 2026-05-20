#include <iostream>
#include <vector>
#include <unordered_map>
#include <cassert>

class Solution {
public:
    std::vector<int> findThePrefixCommonArray(std::vector<int>& A, std::vector<int>& B) {
        int n = A.size();
        std::vector<int> prefixCommonArray(n), frequency(n + 1, 0);
        int commonCount = 0;

        for (int currentIndex = 0; currentIndex < n; ++currentIndex) {
            if (++frequency[A[currentIndex]] == 2) {
                ++commonCount;
                frequency[A[currentIndex]] -= 2;
            }

            if (++frequency[B[currentIndex]] == 2) {
                ++commonCount;
                frequency[B[currentIndex]] -= 2;
            }

            prefixCommonArray[currentIndex] = commonCount;
        }

        return prefixCommonArray;
    }
    std::vector<int> findThePrefixCommonArrayMap(std::vector<int>& A, std::vector<int>& B) {
        std::unordered_map<int, int> umapA, umapB;
        int matches = 0;
        int n = static_cast<int>(B.size());
        std::vector<int> output(n, 0); 
        for (int i = 0; i < n; ++i) {
            ++umapB[B[i]];
            ++umapA[A[i]];
            if (B[i] == A[i]) {
                ++matches;
            } else {
                if (umapB.count(A[i]) > 0) {
                    ++matches;
                    --umapB[A[i]];
                }
                
                if (umapA.count(B[i]) > 0) {
                    ++matches;
                    --umapB[B[i]];
                }
            }
            output[i] = matches;
        }
        return output;
    }
};

int main() {
    Solution sol;
    
    std::vector<int> A = {1, 3, 2, 4}, B = {3, 1, 2, 4};
    std::vector<int> expected_output = {0, 2, 3, 4};
    
    std::vector<int> output = sol.findThePrefixCommonArrayMap(A, B);
    assert((expected_output == output) && "Test #1 failed!");
    
    output = sol.findThePrefixCommonArray(A, B);
    assert((expected_output == output) && "Test #2 failed!");
    
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
