class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
      int maximum = *std::max_element(std::begin(candies), std::end(candies));
      vector<bool> output(candies.size());
      for (int i = 0; i < candies.size(); i++) {
        if (int (candies[i] + extraCandies) >= maximum) {
          output[i] = true;
        } else {
          output[i] = false;
        }
      }
      return output;
    }
};
