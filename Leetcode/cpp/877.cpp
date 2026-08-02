class Solution {
public:
    std::map<std::pair<int, int>, int> umap;

    int dfs(int left, int right, const std::vector<int>& ar) {
        if (left > right) {
            return 0;
        }
        if (umap.contains({left, right})) {
            return umap[{left, right}];
        }
        int left_win = ar[left] - dfs(left + 1, right, ar);
        int right_win = ar[right] - dfs(left, right - 1, ar);
        umap[{left, right}] = std::max(left_win, right_win);
        return umap[{left, right}];
    }

    bool stoneGame(vector<int>& piles) {
        int left = 0;
        int right = piles.size() - 1;
        umap.clear();
        return dfs(left, right, piles) >= 0;
    }
};
