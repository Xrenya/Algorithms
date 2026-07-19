class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        std::vector<int> inorder(numCourses, 0);
        std::unordered_map<int, std::vector<int>> graph;
        for (int i = 0; i < prerequisites.size(); ++i) {
            int need = prerequisites[i][1];
            int take = prerequisites[i][0];
            ++inorder[need];
            graph[take].push_back(need);
        }

        std::deque<int> dq;
        for (int i = 0; i < numCourses; ++i) {
            if (inorder[i] == 0) {
                dq.push_back(i);
            }
        }
        int total = 0;
        while (!dq.empty()) {
            int course = dq.front();

            ++total;
            if (total == numCourses) {
                return true;
            }

            dq.pop_front();
            for (const auto& next : graph[course]) {
                --inorder[next];
                if (inorder[next] == 0) {
                    dq.push_back(next);
                }
            }
        }
        return false;
    }
};
