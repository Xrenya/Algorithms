#include <iostream>
#include <vector>
#include <string>
#include <cassert>
#include <cstring>>


struct TrieNode {
    TrieNode* child[26];
    bool isEnd;
    TrieNode() : isEnd(false) {
        std::memset(child, 0, sizeof(child));
    }
};

class Solution {
public:
    TrieNode* trie = new TrieNode();
    
    void insert(const std::string& word) {
        TrieNode* node = trie;
        for (char ch : word) {
            int idx = ch - 'a';
            if (!node->child[idx]) node->child[idx] = new TrieNode();
            node = node->child[idx];
        }
        node->isEnd = true;
    }

    bool dfs(const std::string& word, int index, TrieNode* node, int changes) {
        if (!node || changes > 2) return false;

        if (index == (int)word.size()) {
            return node->isEnd;
        }

        int idx = word[index] - 'a';

        if (node->child[idx] && dfs(word, index + 1, node->child[idx], changes)) {
            return true;
        }

        if (changes < 2) {
            for (int c = 0; c < 26; ++c) {
                if (c == idx || !node->child[c]) continue;
                if (dfs(word, index + 1, node->child[c], changes + 1)) {
                    return true;
                }
            }
        }

        return false;
    }

    std::vector<std::string> twoEditWords(std::vector<std::string>& queries,
                                          std::vector<std::string>& dictionary) {
        for (const auto& word : dictionary) {
            insert(word);
        }

        std::vector<std::string> output;
        for (const auto& q : queries) {
            if (dfs(q, 0, trie, 0)) {
                output.push_back(q);
            }
        }
        return output;
    }
};


int main()
{
    std::vector<std::string> queries = {"word","note","ants","wood"}, dictionary = {"wood","joke","moat"};
    std::vector<std::string> expected_output = {"word","note","wood"};
    Solution sol;
    std::vector<std::string> output = sol.twoEditWords(queries, dictionary);

    assert(expected_output.size() == output.size() && "Test #1 failed: `output` size is not equal to `expected_output`");
    for (int i = 0; i < output.size(); ++i) {
        assert(expected_output[i] == output[i] && "Test #2 failed: `output` word does not match to `expected_output`");
    }

    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
