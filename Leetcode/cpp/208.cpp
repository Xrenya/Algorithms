class Node {
public:
    std::unordered_map<char, Node*> vocab;
    bool isEnd = false;
};

class Trie {
public:
    Node* node = nullptr;

    Trie() {
        node = new Node();    
    }
    
    void insert(string word) {
        Node* cur = node;
        for (auto letter : word) {
            if (!cur->vocab.contains(letter)) {
                cur->vocab[letter] = new Node;
            }
            cur = cur->vocab[letter];
        }
        cur->isEnd = true; 
    }
    
    bool search(string word) {
        Node* cur = node;
        for (auto letter : word) {
            if (!cur->vocab.contains(letter)) {
                return false;
            }
            cur = cur->vocab[letter];
        }
        return cur->isEnd; 
    }
    
    bool startsWith(string prefix) {
        Node* cur = node;
        for (auto letter : prefix) {
            if (!cur->vocab.contains(letter)) {
                return false;
            }
            cur = cur->vocab[letter];
        }
        return true; 
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
