class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        unordered_map<int, int>m;
        vector<int>result;
        for (int i = 0; i < numbers.size(); i++){
            if (m.find(numbers[i]) == m.end()){
                m[target - numbers[i]] = i + 1;
            }
            else{
                result.push_back(m[numbers[i]]);
                result.push_back(i + 1);
                return result;
            }
        }
        return result;
    }
};

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = numbers.size() - 1;
        vector<int> result;
        while (l < r){
            if (numbers[l] + numbers[r] == target){
                result.push_back(l + 1);
                result.push_back(r + 1);
                break;
            }
            else if (numbers[l] + numbers[r] > target){
                r--;
            }
            else{
                l++;
            }
        }
        return result;
    }
};
