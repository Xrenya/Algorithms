class Solution {
public:
    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
        vector<bool> incomingEdges(n, false);
        for (vector<int>& edge : edges) {
            incomingEdges[edge[1]] = true;
        }
        vector<int> output;
        for (int i = 0; i < n; i++) {
            if (!incomingEdges[i]) {
                output.push_back(i);
            }
        }
        return output;
    }
};
