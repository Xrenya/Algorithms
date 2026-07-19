class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        std::unordered_map<int, std::vector<int>> graph;
        std::unordered_map<int, int> inorder;

        for (int i = 0; i < prerequisites.size(); ++i) {
            int a = prerequisites[i][0];
            int b = prerequisites[i][1];
            ++inorder[a];
            graph[b].push_back(a);
        }
        std::deque<int> dq;
        for (int i = 0; i < numCourses; ++i) {
            if (inorder[i] == 0) {
                dq.push_back(i);
            }
        }
        std::vector<int> output;
        while (!dq.empty()) {
            int course = dq.front();
            dq.pop_front();
            output.push_back(course);
            if (output.size() == numCourses) {
                return output;
            }
            for (const auto next : graph[course]) {
                --inorder[next];
                if (inorder[next] == 0) {
                    dq.push_back(next);
                }
            }
        }
        return {};
    }
};
