class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> ranges;

        for (int i = 0; i < nums.size(); i++) {
            int start = nums[i];
            // Keep iterating until the next element is one more than the current element.
            while (i + 1 < nums.size() && nums[i] + 1 == nums[i + 1]) {
                i++;
            }

            if (start != nums[i]) {
                ranges.push_back(to_string(start) + "->" + to_string(nums[i]));
            } else {
                ranges.push_back(to_string(start));
            }
        }

        return ranges;
    }
};


class Solution {
public:
  string stringfy(int& a, int& b){
    if (a == b) {
      return std::to_string(a);
    } else {
        string arrow = "->";
      return std::to_string(a) + arrow + std::to_string(b);
    }
  }
  vector<string> summaryRanges(vector<int>& nums) {
    vector<string> output;
    if (nums.size() == 0) {
        return output;
    } else if (nums.size() == 1) {
        std::string seq = stringfy(nums[0], nums[0]);
        output.push_back(seq);
        return output;
    }
    int prev = nums[0], last = nums[0];
    for (int i = 1; i < nums.size(); i++) {
      if ((prev + 1) == nums[i]) {
        prev++;
      } else {
        string seq = stringfy(last, prev);
        prev = nums[i];
        last = nums[i];
        output.push_back(seq);
      }
    }
    string seq = stringfy(last, prev);
    output.push_back(seq);
    return output;
  }
};
