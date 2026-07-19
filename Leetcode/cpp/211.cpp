class Node {
public:
    std::unordered_map<char, Node*> vocab;
    bool isEnd = false;
};

class WordDictionary {
public:
    Node* node = nullptr;
    WordDictionary() {
        node = new Node;
    }
    
    void addWord(string word) {
        Node* cur = node;
        for (auto letter : word) {
            if (!cur->vocab.contains(letter)) {
                cur->vocab[letter] = new Node;
            }
            cur = cur->vocab[letter];
        }
        cur->isEnd = true;
    }
    
    bool searchNode(const std::string& word, int index, Node* cur) {
        if (!cur) return false;

        if (index == word.size()) {
            return cur->isEnd;
        }

        char letter = word[index];
        if (letter == '.') {
            for (const auto& [nextLetter, nextNode] : cur->vocab) {
                if (searchNode(word, index + 1, nextNode)) {
                    return true;
                }
            }
            return false;
        } else {
            if (!cur->vocab.contains(letter)) {
                return false;
            }
            return searchNode(word, index + 1, cur->vocab[letter]);
        }
    }

    bool search(string word) {
        return searchNode(word, 0, node);
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */
