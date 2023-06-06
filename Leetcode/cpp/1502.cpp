class Solution {
public:
  bool canMakeArithmeticProgression(vector<int>& arr) {
    int min_value = *min_element(arr.begin(), arr.end());
    int max_value = *max_element(arr.begin(), arr.end());
    int n = arr.size();
    if ((max_value - min_value) == 0) {
      return true;
    } else if ((max_value - min_value) % (n - 1) != 0) {
      return false;
    }
    int diff = (max_value - min_value) / (n - 1);
    unordered_set<int> number_set;
    for (auto num : arr) {
        if ((num - min_value) % diff != 0) {
          return false;
        }
        number_set.insert(num);
    }
    return number_set.size() == n;
  }
};


class Solution {
public:
  bool canMakeArithmeticProgression(vector<int>& arr) {
    std::sort(arr.begin(), arr.end());
    int d = arr[1] - arr[0];
    for (int i = 2; i < arr.size(); i++) {
        if (arr[i] - arr[i - 1] != d) {
            return false;
        }
    }
    return true;
  }
};
