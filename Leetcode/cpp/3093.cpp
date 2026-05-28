#include <iostream>
#include <vector>
#include <array>
#include <string>
#include <climits>

class Solution {
private:
    struct TrieNode {
        array<int, 26> children;
        int best_idx;
        int best_len;
        int best_word_idx;
        
        TrieNode() : best_idx{-1}, best_len{INT_MAX}, best_word_idx{INT_MAX} { children.fill(-1); }
    };

    std::vector<TrieNode> trie;

    void init() {
        trie.clear();
        trie.push_back(TrieNode());
    }

    void update(int node_idx, int length, int idx) {
        auto& node = trie[node_idx];
        if (node.best_idx == -1 || length < node.best_len || (length == node.best_len && idx < node.best_word_idx)) {
            node.best_len = length;
            node.best_word_idx = idx;
            node.best_idx = idx;
        } 
    }

public:
    std::vector<int> stringIndices(std::vector<std::string>& wordsContainer, std::vector<std::string>& wordsQuery) {
        init();

        for (int i = 0; i < wordsContainer.size(); ++i) {
            update(0, wordsContainer[i].length(), i);
        }

        for (int i = 0; i < wordsContainer.size(); ++i) {
            int node = 0;
            std::string& word = wordsContainer[i];

            for (int j = word.length() - 1; j >= 0; j--) {
                int ch = word[j] - 'a';
                if (trie[node].children[ch] == -1) {
                    trie[node].children[ch] = trie.size();
                    trie.push_back(TrieNode());
                }
                node = trie[node].children[ch];
                update(node, word.length(), i);
            }
        }

        std::vector<int> output;
        for (std::string& word : wordsQuery) {
            int node = 0;
            for (int j = word.length() - 1; j >= 0; --j) {
                int ch = word[j] - 'a';
                if (trie[node].children[ch] != -1) {
                    node = trie[node].children[ch];
                } else {
                    break;
                }
            }
            output.push_back(trie[node].best_idx);
        }
        return output;
    }
};
