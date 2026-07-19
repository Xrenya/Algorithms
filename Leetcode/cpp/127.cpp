class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        std::unordered_map<std::string, std::vector<std::string>> graph;
        int size = beginWord.size();
        for (int i = 0; i < wordList.size(); ++i) {
            for (int j = 0; j < size; ++j) {
                std::string word = wordList[i];
                word[j] = '*';
                graph[word].push_back(wordList[i]);
            }
        }
        std::deque<std::pair<std::string, int>> dq{{beginWord, 1}};
        std::unordered_set<std::string> seen;
        seen.insert(beginWord);
        while (!dq.empty()) {
            auto [word, steps] = dq.front();
            if (word == endWord) {
                return steps;
            }
            dq.pop_front();
            for (int i = 0; i < size; ++i) {
                std::string replace = word;
                replace[i] = '*';
                if (graph.contains(replace)) {
                    for (auto next : graph[replace]) {
                        if (!seen.contains(next)) {
                            dq.push_back({next, steps + 1});
                            seen.insert(next);
                        }
                    }
                }
            }
        }
        return 0;
    }
};
