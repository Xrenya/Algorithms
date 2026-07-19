class Solution {
public:
    int minMutation(string startGene, string endGene, vector<string>& bank) {
        std::vector<char> choices{'A', 'C', 'G', 'T'};
        std::deque<std::pair<std::string, int>> dq{{startGene, 0}};
        std::unordered_set<std::string> seen;
        std::unordered_set<std::string> bankSet(bank.begin(), bank.end());

        if (!bankSet.contains(endGene)) {
            return -1;
        }

        seen.insert(startGene);
        
        while (!dq.empty()) {
            auto [node, mutations] = dq.front();
            dq.pop_front();
            if (node == endGene) {
                return mutations;
            }

            for (int i = 0; i < choices.size(); ++i) {
                for (int j = 0; j < startGene.size(); ++j) {
                    std::string newGene = node;
                    newGene[j] = choices[i];
                    if (!seen.contains(newGene) && bankSet.contains(newGene)) {
                        seen.insert(newGene); 
                        dq.push_back({newGene, mutations + 1});
                    }
                }
            }
        }
        return -1;
    }
};
