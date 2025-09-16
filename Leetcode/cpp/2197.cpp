class Solution {
public:
    int find_gcd_euclidean(int a, int b) {
        while (b != 0) {
            int tmp = a;
            a = b;
            b = tmp % b;
        }
        return a;
    }

    int calculate_lcm(int a, int b, int gcd) {
        if ((a == 0) || (b == 0)){
            return 0;
        } else {
            // Calculate LCM using long long to prevent overflow.
            // The formula (a / gcd) * b is safer than (a * b) / gcd.
            return abs(a / gcd) * b;
        }
    }
    vector<int> replaceNonCoprimes(vector<int>& nums) {
        vector<int> output;
        for (auto num : nums) {
            output.push_back(num);
            while (output.size() >= 2) {
                int last = output.back();
                output.pop_back();
                int prev = output.back();
                output.pop_back();
                int gcd = find_gcd_euclidean(last, prev);
                if (gcd > 1) {
                    output.push_back(calculate_lcm(last, prev, gcd));
                } else {
                    output.push_back(prev);
                    output.push_back(last);
                    break;
                }
            } 
        }
        return output;
    }
};

// compact version
#include <vector>
#include <numeric> // Required for std::gcd

class Solution {
public:
    std::vector<int> replaceNonCoprimes(std::vector<int>& nums) {
        std::vector<int> output;
        for (int num : nums) {
            long long current_num = num;
            
            while (!output.empty() && std::gcd((long long)output.back(), current_num) > 1) {
                long long last_num = output.back();
                output.pop_back();
                
                // Calculate LCM using long long to prevent overflow.
                // The formula (a / gcd) * b is safer than (a * b) / gcd.
                long long common_divisor = std::gcd(last_num, current_num);
                current_num = (last_num / common_divisor) * current_num;
            }
            
            output.push_back((int)current_num);
        }
        return output;
    }
};
