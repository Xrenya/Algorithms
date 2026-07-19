class TrieNode {
public:
    TrieNode* children[26] = {nullptr};
    std::string word = "";

};

class Solution {
private:
    void insert(TrieNode* root, const std::string& word) {
        TrieNode* cur = root;
        for (char c : word) {
            int index = c - 'a';
            if (!cur->children[index]) {
                cur->children[index] = new TrieNode;
            }
            cur = cur->children[index];
        }
        cur->word = word;
    }

public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        TrieNode* root = new TrieNode;
        for (const auto& w : words) {
            insert(root, w);
        }

        int ROWS = board.size();
        int COLS = board[0].size();
        std::vector<std::string> output;

        int dirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        
        std::function<void(int, int, TrieNode*)> dfs = [&](int row, int col, TrieNode* node) {
            char letter = board[row][col];
            int index = letter - 'a';

            if (letter == '#' || !node->children[index]) {
                return;
            }

            node = node->children[index];

            if (!node->word.empty()) {
                output.push_back(node->word);
                node->word = "";
            }

            board[row][col] = '#';

            for (int i = 0; i < 4; ++i) {
                int newRow = row + dirs[i][0];
                int newCol = col + dirs[i][1];

                if (newRow >= 0 && newRow < ROWS && newCol >= 0 && newCol < COLS) {
                    dfs(newRow, newCol, node);
                }
            }
            board[row][col] = letter; 
        };

        for (int i = 0; i < ROWS; ++i) {
            for (int j = 0; j < COLS; ++j) {
                dfs(i, j, root);
            }
        }

        return output;
    }
};
