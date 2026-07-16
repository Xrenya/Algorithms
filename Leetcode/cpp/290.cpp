class Solution {
public:
    bool wordPattern(string pattern, string s) {
        std::stringstream ss(s);
        std::string word;
        int index = 0;

        std::unordered_map<char, std::string> char2word;
        std::unordered_map<std::string, char> word2char;
        while (ss >> word) {
            if (index == pattern.length()) {
                return false;
            }
            char chr = pattern[index++];
            if (!char2word.contains(chr) && !word2char.contains(word)) {
                char2word[chr] = word;
                word2char[word] = chr;
            } else if ((!char2word.contains(chr) && word2char.contains(word)) || (char2word.contains(chr) && !word2char.contains(word)) || (char2word[chr] != word || word2char[word] != chr)) {
                return false;
            }
        }
        return index == pattern.length();
    }
};
