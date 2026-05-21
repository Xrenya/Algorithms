#include <iostream>
#include <unordered_map>
#include <vector>
#include <cassert>
#include <memory>


struct TrieUnique {
    int val;
    std::unordered_map<int, std::unique_ptr<TrieUnique>> map;

    TrieUnique() : val(-1) { }
    TrieUnique(int v) : val(v) { }
    // no need for destructor
};

struct Trie {
    int val;
    std::unordered_map<int, Trie*> map;

    Trie() : val(-1) { }
    Trie(int v) : val(v) { }
    
    // Destructor: recursively free all children
    ~Trie() {
        for (auto& [key, child] : map) {
            delete child;    // This triggers child's destructor recursively
        }
    }
};

class Solution {
public:
    int longestCommonPrefix(std::vector<int>& arr1, std::vector<int>& arr2) {
        auto trie = std::make_unique<TrieUnique>();

        for (auto num : arr1) {
            std::vector<int> tmp;
            while (num) {
                tmp.push_back(num % 10);
                num /= 10;
            }
            TrieUnique* cur = trie.get();
            for (int i = tmp.size() - 1; i >= 0; --i) {
                int digit = tmp[i];
                if (!cur->map.contains(digit)) {
                    cur->map[digit] = std::make_unique<TrieUnique>(digit);
                }
                cur = cur->map[digit].get();
            }
        }
        int output = 0;
        for (auto num : arr2) {
            std::vector<int> tmp;
            while (num) {
                tmp.push_back(num % 10);
                num /= 10;
            }
            int length = 0;
            TrieUnique* cur = trie.get();
            for (int i = tmp.size() - 1; i >= 0; --i) {
                int digit = tmp[i];
                if (!cur->map.contains(digit)) {
                    break;
                }
                ++length;
                cur = cur->map[digit].get(); 
            }
            output = std::max<int>(length, output);
        }

        return output;
    }
    
    
    int longestCommonPrefixRaw(std::vector<int>& arr1, std::vector<int>& arr2) {
        Trie* trie = new Trie;

        for (auto num : arr1) {
            std::vector<int> tmp;
            while (num) {
                tmp.push_back(num % 10);
                num /= 10;
            }
            Trie* cur = trie;
            for (int i = tmp.size() - 1; i >= 0; --i) {
                int digit = tmp[i];
                if (!cur->map.contains(digit)) {
                    cur->map[digit] = new Trie(digit);
                }
                cur = cur->map[digit];
            }
        }
        int output = 0;
        for (auto num : arr2) {
            std::vector<int> tmp;
            while (num) {
                tmp.push_back(num % 10);
                num /= 10;
            }
            int length = 0;
            Trie* cur = trie;
            for (int i = tmp.size() - 1; i >= 0; --i) {
                int digit = tmp[i];
                if (!cur->map.contains(digit)) {
                    break;
                }
                ++length;
                cur = cur->map[digit];
            }
            output = std::max<int>(length, output);
        }
        return output;
    }
};


int main() {
    Solution sol;
    std::vector<int> arr1 = {1, 10, 100}, arr2 = {1000};
    int expected_output = 3;
    
    int output = sol.longestCommonPrefix(arr1, arr2);
    assert((expected_output == output) && "Test #1 failed!");
    
    output = sol.longestCommonPrefixRaw(arr1, arr2);
    assert((expected_output == output) && "Test #2 failed!");
    
    std::cout << "Tests are passed!" << std::endl;
    
    return 0;
}
