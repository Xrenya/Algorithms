class Trie {
public:
    bool isEnd = false;
    std::unordered_map<char, Trie*> vocabulary;

    Trie() = default;
    Trie(const Trie& other) {
        this->isEnd = other.isEnd;
        for (const auto& pair : other.vocabulary) {
            this->vocabulary[pair.first] = new Trie(*pair.second);
        }
    }
    Trie& operator=(const Trie& other) {
        if (this != &other) {
            for (auto& pair : vocabulary) delete pair.second;
            vocabulary.clear();

            isEnd = other.isEnd;
            for (const auto& pair : other.vocabulary) {
                vocabulary[pair.first] = new Trie(*pair.second);
            }
        }
        return *this;
    }
    ~Trie() {
        for (auto& pair : vocabulary) {
            delete pair.second;
        }
    }
};

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        Trie trie;
        for (auto str : strs) {
            if (str.empty()) return "";
            Trie* cur = &trie;
            for (auto chr : str) {
                if (cur->vocabulary.find(chr) == cur->vocabulary.end()) {
                    cur->vocabulary[chr] = new Trie();
                }
                cur = cur->vocabulary[chr];
            }
            cur->isEnd = true;
        }
        std::string output;
        Trie* cur = &trie;
        while (!cur->isEnd && cur->vocabulary.size() == 1) {
            auto it = cur->vocabulary.begin();
            output += it->first;
            cur = it->second;
        }
        return output;
    }
};
