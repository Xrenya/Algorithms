class Solution {
public:
    bool exist(const int index, const string& s, const int substring, const int wordLen, const int totalWords, std::unordered_map<std::string, int> umap) {
        int used = 0;
        for (int i = index; i < index + substring; i += wordLen) {
            std::string subWord = s.substr(i, wordLen);
            if (umap.contains(subWord) && umap[subWord] > 0) {
                ++used;
                umap[subWord] -= 1;
            } else {
                return false;
            }
        }
        return used == totalWords;
    }

    vector<int> findSubstring(string s, vector<string>& words) {
        std::unordered_map<std::string, int> umap;
        for (auto word : words) {
            umap[word] += 1;
        }
        int numWords = words.size();
        int lenWord = words[0].length();
        int subStringLen = numWords * lenWord;
        std::vector<int> output;
        for (int index = 0; index < lenWord; ++index) {
            std::unordered_map<std::string, int> window;
            int left = index;
            int counter = 0;
            for (int right = index; right + lenWord <= s.length(); right += lenWord) {
                std::string w = s.substr(right, lenWord);
                ++window[w];
                ++counter;
                while (window[w] > umap[w]) {
                    std::string leftWord = s.substr(left, lenWord);
                    --window[leftWord];
                    --counter;
                    left += lenWord;
                }
                if (counter == numWords) {
                    output.push_back(left);
                }
            }
        }
        return output;
    }
};
