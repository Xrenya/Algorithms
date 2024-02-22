class Solution {
public:
  int findJudge(int n, vector<vector<int>>& trust) {
    vector<int> trusted(n, 0), trusts(n, 0);
    for (int i = 0; i < trust.size(); i++) {
      int from, to;
      from = trust[i][0];
      to = trust[i][1];
      trusted[to - 1]++;
      trusts[from - 1]++;
    }
    for (int i = 0; i < n; i++) {
      if (trusts[i] == 0 && trusted[i] == n - 1) {
        return i + 1;
      }
    }
    return -1;
}
};
