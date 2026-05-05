#include <iostream>
#include <vector>
#include <cassert>

class Solution {
public:
    std::vector<int> finalPrices(std::vector<int>& prices) {
        std::vector<int> stack;
        std::vector<int> output = prices;
        int n = static_cast<int>(prices.size());
        for (int i = 0; i < n; ++i) {
            while (stack.size() > 0 && prices[stack[stack.size() - 1]] >= prices[i]) {
                int index_to_discount = stack[stack.size() - 1];
                stack.pop_back();
                output[index_to_discount] -= prices[i];
            }
            stack.push_back(i);
        }
        return output;
    }
};

int main() {
  Solution sol;
  std::vector<int> prices = {10, 1, 1, 6};
  std::vector<int> expected_output = {9, 0, 1, 6};
  std::vector<int> output = sol.finalPrices(prices);
  assert(output == expected_output && "Test #1 failed!");
  std::cout << "Tests are passed!" << std::endl;
}
