class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
      vector<int> array;
      int push = 0, pop = 0;
      while (push < pushed.size() || pop < popped.size()) {
        if (array.size() != 0 && pop < popped.size() && array.back() == popped[pop]) {
          array.pop_back();
          pop++;
        } else if (push < pushed.size()) {
          array.push_back(pushed[push]);
          push++;
        } else {
          return false;
        }
      }
      return push == pushed.size() && pop == popped.size() ? true : false;
    }
};
